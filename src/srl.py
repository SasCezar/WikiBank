import json
import logging
import multiprocessing
import sys
import time
from functools import partial

from natural.date import compress
from pymongo import MongoClient

import config
from builder import SRLBuilder
from utils import get_chunks


def build(limit, configs):
    builder = SRLBuilder(config.MONGO_IP, config.MONGO_PORT, config.DB, config.WIKIMERGE_COLLECTION,
                         config.SRLMERGE_COLLECTION, config.LANG, config.LANGUAGE)

    return builder.build("id", limit)


def build_srl(configs):
    client = MongoClient(config.MONGO_IP, config.MONGO_PORT)
    db = client[config.DB]
    wikipedia = db[config.WIKIMERGE_COLLECTION]
    documents_id = list(wikipedia.find({}, {"id": 1, "_id": 0}).sort("id"))
    client.close()
    start_time = time.time()
    total = 0
    total_extracted = 0
    total_skipped = 0
    chunks = get_chunks(documents_id, config.CHUNK_SIZE, 'id')
    if config.NUM_WORKERS == 1:
        for chunk in chunks:
            build(chunk, {})
    else:
        pool = multiprocessing.Pool(config.NUM_WORKERS)

        for res in pool.imap(partial(build, configs=configs), chunks):
            total += res['processed']
            if 'extracted' in res:
                total_extracted += res['extracted']
                total_skipped += res['skipped']
                res['total_extracted'] = total_extracted
                res['total_skipped'] = total_skipped
                res['total'] = total
                elapsed = int(time.time() - start_time)
                res['total_elapsed'] = compress(elapsed)
                res['elapsed'] = compress(res['elapsed'])
                logging.info(', '.join("{!s}={!r}".format(key, val) for key, val in res.items()))

        pool.terminate()
    elapsed = int(time.time() - start_time)
    logging.info("Processed {} documents in {} - Total extracted {}".format(total, compress(elapsed), total_extracted))
    return


def relation_contains_verb(relation_position, pos):
    start = relation_position[0]
    end = relation_position[-1] + 1

    if any([True for tag in pos[start:end] if tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']]):
        return True
    else:
        return False


def get_locations(locations):
    pos = [x for k in locations for x in k]
    breaks = []
    if len(locations) > 1:
        i = 0
        for location in locations[:-1]:
            size = len(location)
            breaks.append(size + i)
            i += size

    return pos, breaks


def export(out_path):
    client = MongoClient(config.MONGO_IP, config.MONGO_PORT)
    db = client[config.DB]
    wiki_srl = db[config.SRLMERGE_COLLECTION]
    documents = wiki_srl.find({}, {"_id": 0, "text": 0})
    i = 0
    sk = 0
    nv_count = 0
    with open(out_path, "wt", encoding="utf8", newline="") as outf:
        for document in documents:
            for sentence_id in document['sentences']:
                sentence = document['sentences'][sentence_id]
                text = sentence['sentence']
                pos = sentence['pos']
                try:
                    entity_locations, breaks = get_locations(sentence['full_match_entity_location'])
                    if breaks:
                        raise Exception
                except:
                    i += 1
                    continue

                out_doc = {'lang': config.LANG, 'id': sentence_id, 'sentence': text, 'entity': document['label'],
                           'sentence_sequence': sentence['sentence_sequence'], 'pos': pos, 'entity_id': document['id'],
                           'entity_sequence': document['label_sequence'], 'relations': [],
                           'entity_locations': entity_locations}

                for relation in sentence['relations']:
                    if not relation_contains_verb(relation['relation_location'][0], pos):
                        nv_count += 1
                        continue
                    answer_locations, answer_locations_breaks = get_locations(relation['answer_location'])
                    relation_locations, relation_locations_breaks = get_locations(relation['relation_location'])
                    if answer_locations_breaks or relation_locations_breaks:
                        continue
                    rel_doc = {'property_id': relation['prop_id'], 'relation_sequence': relation['relation_sequence'],
                               'property_label': relation['relation'], 'relation_locations': relation_locations,
                               # 'relation_locations_breaks': relation_locations_breaks,
                               'sentence_relation': relation['sentence_relation'], 'answer_id': relation['answer_id'],
                               'answer': relation['answer'], 'answer_locations': answer_locations,
                               # 'answer_location_breaks': answer_locations_breaks,
                               'answer_sequence': relation['answer_sequence'], 'relation_id': relation['id']}

                    out_doc['relations'].append(rel_doc)

                if out_doc['relations']:
                    obj = json.dumps(out_doc, ensure_ascii=False)
                    outf.write(obj + "\n")
                else:
                    if nv_count:
                        sk += 1
                    i += 1

    print(i)
    print(nv_count)
    print(sk)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("Running %s", " ".join(sys.argv))
    build_srl({})
    export("{}_srl.json".format(config.LANG))
    logging.info("Completed %s", " ".join(sys.argv))
