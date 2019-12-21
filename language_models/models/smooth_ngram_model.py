from nltk import ConditionalFreqDist, ConditionalProbDist, LidstoneProbDist
from collections import defaultdict


class SmoothNgramModel(object):

    def __init__(self, data_set, n, gamma):
        self.data_set = data_set.split()
        self.model = defaultdict(lambda: defaultdict(lambda: 0))
        self.gamma = gamma
        self.n = n

    def generate_next_word(self, ngram):
        probability = 0
        word_to_return = False
        for model_ngram in self.model:
            if model_ngram == ngram:
                word_to_return = self.model[model_ngram].max()
        return word_to_return

    def run(self):
        cfd = ConditionalFreqDist((tuple(self.data_set[i: i + self.n - 1]), self.data_set[i + self.n - 1]) for i in
                                  range(len(self.data_set) - self.n + 1))
        lidstone_estimator = lambda fd: LidstoneProbDist(fd, self.gamma, fd.B() + 1)
        cpd = ConditionalProbDist(cfd, lidstone_estimator)
        self.model = cpd

    def measure_perplexity(self, testset):
        with open(testset, 'r') as f:
            testset_content = f.read().replace('\n', ' ')
        testset_content = testset_content.split()
        perplexity = 1
        n = 0
        index = -1
        for ngram in self.model:
            look_back_size = len(ngram)
            break
        for word in testset_content:
            n += 1
        for word in testset_content:
            index += 1
            ngram = ()
            next_iter = False
            for i in range(look_back_size):
                if index - i - 1 >= 0:
                    ngram = (testset_content[index - i - 1],) + ngram
                else:
                    next_iter = True
            if next_iter:
                continue
            perplexity = perplexity * pow((1 / self.model[ngram].prob(word)), 1 / float(n))
        return perplexity
