from language_models.models.ngram_model import NgramModel
import os

cwd = os.getcwd()

PATH_FOR_TEST = cwd + "\\dal\\test.txt"


def train_word_lm(data_set, n=2):
    # TODO WRITE THIS IN THE NOTEBOOK - also in the notebook need to answer the question under 1.2.2
    with open(data_set, "r") as file:
        content = file.read().replace('\n', ' ')
    my_model = NgramModel(content, n)
    my_model.run()
    return my_model


# for testing purpose
if __name__ == "__main__":
    test_model = train_word_lm(PATH_FOR_TEST, n=4)
    print(test_model.model[('adi', 'krasin', 'is')]['the'])
