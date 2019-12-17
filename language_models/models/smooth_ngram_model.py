from nltk import ngrams
from collections import defaultdict


# TODO - FOR NOW THIS IS THE ADD-K WITH K=1 SMOOTHING (THIS SUCKS - NEED TO MAKE A BETTER SMOOTHING BUT NEED HELP)
class SmoothNgramModel(object):

    def __init__(self, data_set, n):
        self.data_set = data_set
        self.model = defaultdict(lambda: defaultdict(lambda: 1))
        self.n = n

    def generate_next_word(self, ngram):
        probability = 0
        word_to_return = False
        for word in self.model[ngram]:
            if self.model[ngram][word] > probability:
                word_to_return = word
                probability = self.model[ngram][word]
        return word_to_return

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
            perplexity = perplexity * (1 / self.model[ngram][word])
        perplexity = pow(perplexity, 1 / float(n))
        return perplexity
