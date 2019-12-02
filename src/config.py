import os

from date_formatter import DateFormatterFactory
from tokenizers import SpacyTokenizer

LANG = 'en'
LANGUAGE = 'english'
LOCALE = 'en-US'

NUM_WORKERS = 5
CHUNK_SIZE = 1000

MONGO_IP = "localhost"
MONGO_PORT = 27017
DB = "WikiSRL"
WIKIDATA_COLLECTION = "wikidata"
WIKIPEDIA_COLLECTION = "{}wiki".format(LANG)
WIKIMERGE_COLLECTION = "{}wiki_merged".format(LANG)
SRLMERGE_COLLECTION = "{}wiki_srl".format(LANG)

TOKENIZER = SpacyTokenizer(LANG, disable=['parser', 'ner', 'textcat', 'tagger'])
DATE_FORMATTER = DateFormatterFactory.get_formatter(lang=LANG, out_locale=LOCALE)
