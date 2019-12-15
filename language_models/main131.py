from language_models.main121 import train_word_lm
import os

cwd = os.getcwd()
PATH_FOR_TEST = cwd + "\\dal\\test.txt"
PATH_FOR_TEST2 = cwd + "\\dal\\test2.txt"


def measure_perplexity(testset, model):
    with open(testset, 'r') as f:
        testset_content = f.read().replace('\n', '')
    testset_content = testset_content.split()
    perplexity = 1
    n = 0
    for word in testset_content:
        n += 1
        for ngram in model:
            # escaping from division by 0
            if model[ngram][word]:
                perplexity = perplexity * (1/model[ngram][word])
    perplexity = pow(perplexity, 1/float(n))
    return perplexity


# for testing purpose
if __name__ == '__main__':
    test_model = train_word_lm(PATH_FOR_TEST)
    perplexity_res1 = measure_perplexity(PATH_FOR_TEST, test_model)
    perplexity_res2 = measure_perplexity(PATH_FOR_TEST2, test_model)
    print(perplexity_res1)
    print(perplexity_res2)
