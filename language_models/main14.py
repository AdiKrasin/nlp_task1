import os
from collections import *
from random import random

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal"


def generate_letter(lm, history, order):
        history = history[-order:]
        dist = lm[history]
        x = random()
        for c, v in dist:
            x = x - v
            if x <= 0:
                return c


class SplitDataSet:

    def __init__(self, dataset_full_path):
        with open(dataset_full_path, 'r') as f:
            self.dataset = f.read()

    def split(self):
        dataset_len = len(self.dataset)
        train_len = int(dataset_len * 0.8)
        dev_len = int(dataset_len * 0.1)
        train_content = self.dataset[:train_len]
        dev_content = self.dataset[train_len:train_len+dev_len]
        valid_content = self.dataset[train_len+dev_len:]
        return train_content, dev_content, valid_content


def train_char_lm(content, order=20):
    data = content
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char] += 1

    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c, cnt/s) for c, cnt in counter.items()]
    outlm = {hist: normalize(chars) for hist, chars in lm.items()}
    return outlm


def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in range(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)


def perplexity(lm, dataset, order):
    data = dataset
    perplexity = 1
    n = 0
    for i in range(len(data) - order):
        n += 1
    for i in range(len(data) - order):
        history, char = data[i:i + order], data[i + order]
        perplexity = perplexity * pow((1 / lm[history][char]), 1 / float(n))
    return perplexity


if __name__ == "__main__":
    split_dataset = SplitDataSet(DATA_SET_PATH+"\\cooking.txt")
    train, dev, valid = split_dataset.split()
    lm = train_char_lm(train)
    perplexity_res = perplexity(lm, valid, 20)
    print(perplexity_res)
