import hashlib
import itertools
import re
import time
import traceback
from abc import ABC, abstractmethod
from collections import Counter, defaultdict

import nltk
from ftfy import fix_text
from nltk.tokenize.moses import MosesTokenizer
from pymongo import MongoClient

from article_extractors import ArticleExtractorFactory


class Builder(ABC):
    def __init__(self, ip, port, db, source, destination, batch_size=500):
        self._client = MongoClient(ip, port)
        self._db = self._client[db]
        self._source = self._db[source]
        self._destination = self._db[destination]
        self._batch_size = batch_size

    def build(self, key, limit, **kwargs):
        n = 0
        processed = []
        mask = kwargs['mask'] if 'mask' in kwargs else {"_id": 0}
        start_time = time.time()
        counter = Counter()
        for doc in self._source.find({key: {"$gte": limit[0], "$lte": limit[1]}}, mask):
            # for doc in self._source.find({key: {"$in": limit}}, mask):
            try:
                result = self._build(doc)
            except:
                traceback.print_exc()
                continue

            if result:
                document = result['document']
                counter.update(result['stats'])
                processed.append(document)
                n += 1

            if len(processed) >= self._batch_size:
                self._destination.insert_many(processed, ordered=False, bypass_document_validation=True)
                n += len(processed)
                processed = []

        if processed:
            self._destination.insert_many(processed, ordered=False, bypass_document_validation=True)
            n += len(processed)
        elapsed = int(time.time() - start_time)
        res = {"processed": n, "elapsed": elapsed}
        res.update(counter)

        return res

    @abstractmethod
    def _build(self, doc, **kwargs):
        return doc

    @staticmethod
    def _get_id(string):
        return hashlib.sha1(string.encode("utf-8")).hexdigest()


class SRLBuilder(Builder):

    def __init__(self, ip, port, db, source, destination, lang, language):
        super().__init__(ip, port, db, source, destination)
        self._sent_tokenizer = nltk.sent_tokenize
        self._word_tokenizer = MosesTokenizer(lang)
        self._pos_tagger = nltk.pos_tag
        self._language = language

    def _build(self, doc, **kwargs):
        text = doc['text'].strip()
        if not text:
            return {}

        sentences = self._sent_tokenizer(text.replace("\n\n", "\n"), language=self._language)
        srl = {"id": doc['id'], "text": doc['text'], "label": doc['label'],
               "label_sequence": self._tokenize(doc['label']),
               'sentences': defaultdict(lambda: {"sentence": "", "sentence_sequence": [], "relations": []})}

        extracted = 0
        skipped = 0
        seen = set()
        for prop in doc['facts']:
            relation = doc['properties'][prop]
            prop_labels = relation.get('aliases', [])
            prop_labels.append(relation['label'])
            for fact in doc['facts'][prop]:
                answer = fact['value']
                sentence, sentence_relation = self._distant_supervision(answer, srl['label'], prop_labels, sentences)

                if not sentence:
                    continue

                sentence_id = self._get_id(sentence)
                if sentence_id not in seen:
                    sentence_sequence = self._tokenize(sentence)
                    pos = self._pos_tagger(sentence_sequence, lang=self._language)
                    srl['sentences'][sentence_id]['sentence'] = sentence
                    srl['sentences'][sentence_id]['sentence_sequence'] = sentence_sequence
                    srl['sentences'][sentence_id]['pos'] = [tag for _, tag in pos]
                    entity_location = self.find_full_matches(sentence_sequence, srl['label_sequence'])
                    if not entity_location:
                        # print("Unable to find {} in sequence {}".format(srl["label_sequence"], sentence_sequence))
                        skipped += 1
                        continue
                    extracted += 1
                    srl['sentences'][sentence_id]['full_match_entity_location'] = entity_location
                    seen.add(sentence_id)
                else:
                    sentence_sequence = srl['sentences'][sentence_id]['sentence_sequence']

                answer_sequence = self._tokenize(fact['value'])
                answer_location = self.find_full_matches(sentence_sequence, answer_sequence)
                if not answer_location:
                    # print("Unable to find {} in sequence {}".format(answer_sequence, sentence_sequence))
                    skipped += 1
                    continue

                relation_sequence = self._tokenize(sentence_relation)
                relation_location = self.find_full_matches(sentence_sequence, relation_sequence)
                if not relation_location:
                    # print("Unable to find {} in sequence {}".format(relation_sequence, sentence_sequence))
                    skipped += 1
                    continue

                triple = {"relation": relation['label'], "answer": fact['value'],
                          "answer_sequence": answer_sequence, 'answer_location': answer_location,
                          "id": self._get_id_for_qa(doc['id'], prop, fact['id']),
                          "answer_id": fact['id'], "prop_id": prop, "sentence_relation": sentence_relation,
                          "relation_sequence": relation_sequence, "relation_location": relation_location,
                          "type": fact['type']}

                srl['sentences'][sentence_id]['relations'].append(triple)
        if not len(srl['sentences']):
            return {}
        return {"document": srl, "stats": {"extracted": extracted, "skipped": skipped}}

    @staticmethod
    def _distant_supervision(answer, entity, relations, sentences):
        e_template = "\\b" + re.escape(entity) + "\\b"
        a_template = "\\b" + re.escape(answer) + "\\b"
        r_template = "(?P<relation>" + "|".join(["\\b" + re.escape(relation) + "\\b" for relation in relations]) + ")"
        for sentence in sentences:
            relation = re.search(r_template, sentence)
            if re.search(e_template, sentence) and re.search(a_template, sentence) and relation:
                return sentence, relation.group("relation")

        return False, False

    def _get_id_for_qa(self, page_id, prop_id, answer_id):
        unique_str = " ".join([page_id, prop_id, answer_id])
        return self._get_id(unique_str)

    def _tokenize(self, sentence):
        sentence = sentence.replace("\n", "")
        return [fix_text(t) for t in self._word_tokenizer.tokenize(sentence)]

    @staticmethod
    def find_full_matches(iterable, sublist):
        results = []
        sll = len(sublist)
        for ind in (i for i, e in enumerate(iterable) if e == sublist[0]):
            if iterable[ind:ind + sll] == sublist:
                results.append(list(range(ind, ind + sll)))

        return results


class WikiReadingBuilder(Builder):
    def __init__(self, ip, port, db, source, destination):
        super().__init__(ip, port, db, source, destination)
        self._tokenizer = lambda x: x.split()  # SlingTokenizer()
        self._pos_tagger = nltk.pos_tag

    def _build(self, doc, **kwargs):
        text = doc['text'].strip()
        if not text:
            return {}

        self._tokenize(doc)
        wikireading_doc = {'answer_breaks': [], 'answer_ids': ['IDs'], 'answer_location': [],
                           'answer_sequence': ['IDs'], 'answer_string_sequence': [], 'break_levels': [],
                           'document_sequence': ['IDs'], 'full_match_answer_location': [],
                           'paragraph_breaks': doc['paragraph_breaks'], 'question_sequence': ['IDs'],
                           'question_string_sequence': [],
                           'raw_answer_ids': ['IDs'], 'raw_answers': '', 'sentence_breaks': doc['sentence_breaks'],
                           'string_sequence': doc['string_sequence'], 'type_sequence': ['IDs']}

        for prop in doc['facts']:
            question = doc['properties'][prop]
            answer_string_sequence = []
            answer_breaks = []
            raw_answers = []
            full_match_answer_location = []
            answer_location = []
            for fact in doc['facts'][prop]:
                if answer_string_sequence:
                    answer_breaks.append(len(answer_string_sequence))
                raw_answers.append(fact['value'])
                answer = fact['value_sequence']
                answer_string_sequence += answer
                full_match_answer_location += self.find_full_matches(wikireading_doc["string_sequence"], answer)
                answer_location += self.find_matches(wikireading_doc["string_sequence"], answer)

            wikireading_doc['answer_breaks'] = answer_breaks
            wikireading_doc['answer_location'] = answer_location
            wikireading_doc['answer_string_sequence'] = answer_string_sequence
            wikireading_doc['full_match_answer_location'] = full_match_answer_location
            wikireading_doc['question_string_sequence'] = question['label_sequence']
            return wikireading_doc

    def _tokenize(self, document):
        article_text = document['text'].strip()
        tokens, break_levels, _ = self._tokenizer.tokenize(article_text)
        document['string_sequence'] = tokens
        document['break_levels'] = break_levels
        document['sentence_breaks'] = [i for i, brk in enumerate(break_levels) if brk >= 3]
        document['paragraph_breaks'] = [i for i, brk in enumerate(break_levels) if brk == 4]

        assert len(tokens) == len(break_levels)

        tokens, _, _ = self._tokenizer.tokenize(document['label'])
        document['label_sequence'] = tokens

        for prop in document['properties']:
            tokens, _, _ = self._tokenizer.tokenize(document['properties'][prop]['label'])
            document['properties'][prop]['label_sequence'] = tokens

        for prop in document['facts']:
            for fact in document['facts'][prop]:
                tokens, _, _ = self._tokenizer.tokenize(fact['value'])
                if len(tokens) == 0:
                    tokens = fact['value']
                fact['value_sequence'] = tokens

    @staticmethod
    def find_matches(sequence, answer):
        elements = set(answer)
        return [index for index, value in enumerate(sequence) if value in elements]

    def find_full_matches(self, list, sublist):
        results = []
        sll = len(sublist)
        for ind in (i for i, e in enumerate(list) if e == sublist[0]):
            if list[ind:ind + sll] == sublist:
                results.append(range(ind, ind + sll))

        return results

    @staticmethod
    def is_sublist(sublist, list):
        sll = len(sublist)
        try:
            for ind in (i for i, e in enumerate(list) if e == sublist[0]):
                if list[ind:ind + sll] == sublist:
                    return True
        except IndexError:
            print(sublist)
            print(list)
            raise
        return False
