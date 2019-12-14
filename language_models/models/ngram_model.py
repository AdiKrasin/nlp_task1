from nltk import ngrams
from collections import defaultdict


class NgramModel:

    def __init__(self, data_set, n):
        self.data_set = data_set
        self.model = defaultdict(lambda: defaultdict(lambda: 0))
        self.n = n

    def run(self):
        for gram in ngrams(self.data_set.split(), self.n, pad_right=True, pad_left=True):
            self.model[gram[:-1]][gram[-1]] += 1
        for w1_wn_minus_1 in self.model:
            total_count = float(sum(self.model[w1_wn_minus_1].values()))
            for wn in self.model[w1_wn_minus_1]:
                self.model[w1_wn_minus_1][wn] /= total_count
