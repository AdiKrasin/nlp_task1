from language_models.main121 import train_word_lm
import os
import random
from language_models.dal.gather_data_handler import GatherDataHandler

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = cwd + "\\dal\\data_set_unpacked"


PATH_FOR_TEST = cwd + "\\dal\\random_content"


def generate(model, seed):
    with open(seed, "r") as file:
        content = file.read().replace('\n', ' ')
    split_content = content.split()
    range_list = range(len(split_content))
    random_index = random.choice(range_list)
    prefix = ""
    for i in range(19):
        if random_index in range(len(split_content)):
            prefix += " " + split_content[random_index]
        else:
            return prefix
        random_index += 1
    prefix = prefix[1:]
    prefix_as_n_gram = tuple(prefix.split())
    next_word = True
    while next_word:
        next_word = model.generate_next_word(prefix_as_n_gram[-19:])
        if next_word:
            prefix_as_n_gram += (next_word, )
    text = ""
    for i in range(len(prefix_as_n_gram)):
        text += " " + prefix_as_n_gram[i]
    return text[1:]


# for testing purpose
if __name__ == '__main__':
    GD = GatherDataHandler(10000, path_to_data_set=DATA_SET_PATH, path_to_unpack=UNPACK_PATH)
    GD.extract_all()
    actual_model = train_word_lm(UNPACK_PATH + "\\simple-examples\\data\\ptb.train.txt", n=20, smooth=True, gamma=0.9)
    created_text1 = generate(actual_model, PATH_FOR_TEST+".txt")
    GD.clean()
    print(created_text1)
