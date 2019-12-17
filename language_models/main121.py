from language_models.models.ngram_model import NgramModel
from language_models.models.smooth_ngram_model import SmoothNgramModel
import os

cwd = os.getcwd()

PATH_FOR_TEST = cwd + "\\dal\\test.txt"


def train_word_lm(data_set, n=2, smooth=False):
    with open(data_set, "r") as file:
        content = file.read().replace('\n', ' ')
    if not smooth:
        my_model = NgramModel(content, n)
    else:
        my_model = SmoothNgramModel(content, n)
    my_model.run()
    return my_model


# for testing purpose
if __name__ == "__main__":
    actual_model = train_word_lm(PATH_FOR_TEST, n=4)
    print(actual_model.model[('adi', 'krasin', 'is')]['the'])

