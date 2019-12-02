import argparse
import copy
import csv
import json
import logging
import sys


def format_conll(in_path, out_path, lang):
    with open(in_path, "rt", encoding="utf8") as inf, open(out_path, "wt", encoding="utf8", newline="") as outf:
        writer = csv.writer(outf, delimiter="\t", quotechar="", quoting=csv.QUOTE_NONE)
        for line in inf:
            obj = json.loads(line)
            sentence = ["#TASK", "#LANG"] + obj['sentence_sequence']
            entity_locations = obj['entity_locations']

            tags = ["WD-SRL", lang] + ['O'] * (len(sentence) - 2)
            for entity_location in entity_locations:
                tags[entity_location + 2] = "A1"

            relations = obj['relations']
            for relation in relations:
                stags = copy.deepcopy(tags)
                prop = relation['property_id']
                for relation_location in relation['relation_locations']:
                    stags[relation_location + 2] = prop

                for answer_location in relation['answer_locations']:
                    stags[answer_location + 2] = "A2"

                assert len(sentence) == len(stags)
                for key, value in zip(sentence, stags):
                    assert "\t" not in key
                    assert "\t" not in value
                    writer.writerow([key, value])

                writer.writerow([])


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("Running %s", " ".join(sys.argv))

    parser = argparse.ArgumentParser(description="Builds a parallel corpus on entities.")
    parser.add_argument('-f', '--file', help='Languages used to create a parallel split', required=True)
    parser.add_argument('-o', '--out', help='Out path', required=True)
    parser.add_argument('-l', '--lang', help='Language of the files', required=True)

    args = parser.parse_args()

    format_conll(args.file, args.out, args.lang)
    logging.info("Exporting complete")
    logging.info("Completed %s", " ".join(sys.argv))
