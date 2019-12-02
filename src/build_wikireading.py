import logging
import multiprocessing
import sys
import time

from natural.date import compress
from pymongo import MongoClient

import config
from sling_tokenizer import SlingTokenizer
from utils import find_full_matches, find_matches, get_chunks

tokenizer = SlingTokenizer()


def tokenize(document):
    article_text = document['text'].strip()
    tokens, break_levels, _ = tokenizer.tokenize(article_text)
    document['string_sequence'] = tokens
    document['break_levels'] = break_levels
    document['sentence_breaks'] = [i for i, brk in enumerate(break_levels) if brk >= 3]
    document['paragraph_breaks'] = [i for i, brk in enumerate(break_levels) if brk == 4]

    tokens, _, _ = tokenizer.tokenize(document['label'])
    document['label_sequence'] = tokens

    for prop in document['properties']:
        tokens, _, _ = tokenizer.tokenize(document['properties'][prop]['label'])
        document['properties'][prop]['label_sequence'] = tokens

    for prop in document['facts']:
        for fact in document['facts'][prop]:
            tokens, _, _ = tokenizer.tokenize(fact['value'])
            if len(tokens) == 0:
                tokens = fact['value']
            fact['value_sequence'] = tokens

    return document


def build(limit):
    client = MongoClient(config.MONGO_IP, config.MONGO_PORT)
    db = client[config.DB]
    wikimerge = db[config.WIKIMERGE_COLLECTION]
    wikireading = db['test_wikireading']

    n = 0
    processed = []
    start_time = time.time()
    for pa in wikimerge.find({"id": {"$gte": limit[0], "$lte": limit[1]}}, {"_id": 0}):
        text = pa['text'].strip()
        if not text:
            continue

        page = tokenize(pa)
        n += 1
        wikireading_doc = {'answer_breaks': [], 'answer_ids': ['IDs'], 'answer_location': [],
                           'answer_sequence': ['IDs'], 'answer_string_sequence': [], 'break_levels': [],
                           'document_sequence': ['IDs'], 'full_match_answer_location': [],
                           'paragraph_breaks': page['paragraph_breaks'], 'question_sequence': ['IDs'],
                           'question_string_sequence': [],
                           'raw_answer_ids': ['IDs'], 'raw_answers': '', 'sentence_breaks': page['sentence_breaks'],
                           'string_sequence': page['string_sequence'], 'type_sequence': ['IDs']}

        for prop in page['facts']:
            question = page['properties'][prop]
            answer_string_sequence = []
            answer_breaks = []
            raw_answers = []
            full_match_answer_location = []
            answer_location = []
            for fact in page['facts'][prop]:
                if answer_string_sequence:
                    answer_breaks.append(len(answer_string_sequence))
                raw_answers.append(fact['value'])
                answer = fact['value_sequence']
                answer_string_sequence += answer
                full_match_answer_location += find_full_matches(wikireading_doc["string_sequence"], answer)
                answer_location += find_matches(wikireading_doc["string_sequence"], answer)

            wikireading_doc['answer_breaks'] = answer_breaks
            wikireading_doc['answer_location'] = answer_location
            wikireading_doc['answer_string_sequence'] = answer_string_sequence
            wikireading_doc['full_match_answer_location'] = full_match_answer_location
            wikireading_doc['question_string_sequence'] = question['label_sequence']

            processed.append(wikireading_doc)

        if len(processed) > 500:
            wikireading.insert_many(processed, ordered=False, bypass_document_validation=True)
            processed = []

    if processed:
        wikireading.insert_many(processed, ordered=False, bypass_document_validation=True)

    elapsed = int(time.time() - start_time)
    res = {"processed": n, "elapsed": elapsed}
    return res


def wikireading():
    client = MongoClient(config.MONGO_IP, config.MONGO_PORT)
    db = client[config.DB]
    wikipedia = db[config.WIKIPEDIA_COLLECTION]
    wikidocs = list(wikipedia.find({}, {'wikidata_id': 1, '_id': 0}).sort('wikidata_id'))
    chunks = get_chunks(wikidocs, config.CHUNK_SIZE, 'wikidata_id')
    del wikidocs
    start_time = time.time()
    total = 0

    if config.NUM_WORKERS == 1:
        for chunk in chunks:
            build(chunk)
    else:
        chunks = [(x.decode(), y.decode()) for x, y in chunks]
        pool = multiprocessing.Pool(config.NUM_WORKERS)
        for res in pool.imap(build, chunks):
            total += res['processed']
            res['total'] = total
            part = int(time.time() - start_time)
            res['elapsed'] = compress(res['elapsed'])
            res['total_elapsed'] = compress(part)
            logging.info("Processed {processed} ({total} in total) documents in {elapsed} (running time {"
                         "total_elapsed})".format(**res))

        pool.terminate()

    elapsed = int(time.time() - start_time)
    logging.info("Processed {} documents in {}".format(total, compress(elapsed)))
    return


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)

    logging.info("Running %s", " ".join(sys.argv))
    wikireading()
    logging.info("Completed %s", " ".join(sys.argv))
