#!/usr/bin/env python

import argparse
import csv
import nltk
import os
import re
import string


def _setup():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    tokenizer_dir = "{root_dir}/{nltk_punkt}".format(root_dir=root_dir, nltk_punkt='lib/nltk_data')
    tokenizer_path = "{root_dir}/{nltk_punkt}".format(root_dir=root_dir, nltk_punkt='lib/nltk_data/tokenizers/punkt/PY3/')
    content = os.listdir(tokenizer_dir)
    nltk.data.path.append(tokenizer_path)

    if (len(content) > 1):
        return
    else:
        download_path = "{root_dir}/{lib}".format(root_dir=root_dir, lib='lib/nltk_data')
        nltk.download('punkt', download_path)

    print('Setup complete.')


def _tokenize(file):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    tokenizer_path = "nltk:{root_dir}/{nltk_punkt}".format(root_dir=root_dir, nltk_punkt='lib/nltk_data/tokenizers/punkt/PY3/english.pickle')

    tokenizer = nltk.data.load(tokenizer_path)
    with open(file, 'r') as input:
        content = input.read()

    return tokenizer.tokenize(content)


def _index(sentences):
    order = list()
    table = dict()
    pattern = re.compile('([\w\d]+)')

    for sentence_idx, sentence in enumerate(sentences):
        tokens = re.findall('\S+', sentence)

        for token_idx, token in enumerate(tokens):
            token = pattern.search(token).group(1)
            token = token.lower()

            if token in table:
                table[token]['frequency'] += 1
                table[token]['occurrences'].append(sentence_idx)
            else:
                order.append(token)
                table[token] = {'frequency': 1, 'occurrences': [sentence_idx]}

    order.sort()
    return (order, table)


def _save(order, table, file):
    with open(file, 'w', newline='') as output:
        writer = csv.writer(output, dialect='excel', delimiter='\t')
        writer.writerow(['', 'Word', 'Frequency', 'Occurrences'])

        for idx, word in enumerate(order):
            alpha_cnt = 26
            serial = idx % alpha_cnt
            serial_cnt = (idx // alpha_cnt) + 1
            serial_id = string.ascii_lowercase[serial] * serial_cnt
            occurrences_str = ', '.join(str(i) for i in table[word]['occurrences'])

            writer.writerow([serial_id, word, table[word]['frequency'], occurrences_str])

    msg = "Created concordance at {file}".format(file=file)
    print(msg)


def _main(args):
    sentences = _tokenize(args.corpus)
    (order, table) = _index(sentences)
    _save(order, table, args.concordance)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='concordance')
    parser.add_argument('corpus')
    parser.add_argument('concordance')
    args = parser.parse_args()

    _setup()
    _main(args)
