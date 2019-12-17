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

    def measure_perplexity(self, testset):
        with open(testset, 'r') as f:
            testset_content = f.read().replace('\n', ' ')
        testset_content = testset_content.split()
        perplexity = 1
        n = 0
        infinity = False
        index = -1
        for ngram in self.model:
            look_back_size = len(ngram)
            break
        for word in testset_content:
            index += 1
            n += 1
            ngram = ()
            for i in range(look_back_size):
                if index - i - 1 >= 0:
                    ngram = (testset_content[index - i - 1],) + ngram
                else:
                    ngram = (None,) + ngram
            # escaping from division by 0
            if self.model[ngram][word]:
                perplexity = perplexity * (1 / self.model[ngram][word])
            else:
                infinity = True
        perplexity = pow(perplexity, 1 / float(n))
        return perplexity, infinity
