from language_models.main121 import train_word_lm
import os

cwd = os.getcwd()
PATH_FOR_TEST = cwd + "\\dal\\test.txt"
PATH_FOR_TEST2 = cwd + "\\dal\\test2.txt"


def measure_perplexity(testset, model):
    with open(testset, 'r') as f:
        testset_content = f.read().replace('\n', ' ')
    testset_content = testset_content.split()
    perplexity = 1
    n = 0
    infinity = False
    index = -1
    for ngram in model:
        look_back_size = len(ngram)
    # TODO THIS ONLY WORKS FOR NGRAM MODELS - CHECK IF THAT IS OK!
    for word in testset_content:
        index += 1
        n += 1
        ngram = ()
        for i in range(look_back_size):
            if index-i-1 >= 0:
                ngram = (testset_content[index-i-1],) + ngram
            else:
                ngram = (None,) + ngram
        # escaping from division by 0
        if model[ngram][word]:
            perplexity = perplexity * (1/model[ngram][word])
        else:
            infinity = True
    perplexity = pow(perplexity, 1/float(n))
    return perplexity, infinity


# TODO NEED TO ALSO DO THIS:  Adapt the methods to compute the cross-entropy and perplexity of a model from
#  nltk.model.ngram to your implementation and measure the reported perplexity values on the Penn Treebank validation
#  dataset ptb.valid.txt. AND I DON'T UNDERSTAND WHAT DOES IT MEAN


# for testing purpose
if __name__ == '__main__':
    test_model = train_word_lm(PATH_FOR_TEST, n=3)
    perplexity_res1, infinity1 = measure_perplexity(PATH_FOR_TEST, test_model)
    perplexity_res2, infinity2 = measure_perplexity(PATH_FOR_TEST2, test_model)
    if not infinity1:
        print(perplexity_res1)
    else:
        print("infinity")
    if not infinity2:
        print(perplexity_res2)
    else:
        print("infinity")
