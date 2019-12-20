from language_models.main121 import train_word_lm
import os
import random

cwd = os.getcwd()
PATH_FOR_TEST = cwd + "\\dal\\random_content.txt"
PATH_FOR_TEST2 = cwd + "\\dal\\random_content2.txt"


def generate(model, seed):
    with open(seed, "r") as file:
        content = file.read().replace('\n', ' ')
    split_content = content.split()
    range_list = range(len(split_content))
    random_index = random.choice(range_list)
    prefix = ""
    for i in range(9):
        if random_index in range(len(split_content)):
            prefix += " " + split_content[random_index]
        else:
            return prefix
        random_index += 1
    prefix = prefix[1:]
    prefix_as_n_gram = tuple(prefix.split())
    next_word = True
    while next_word:
        next_word = model.generate_next_word(prefix_as_n_gram[-9:])
        if next_word:
            prefix_as_n_gram += (next_word, )
    text = ""
    for i in range(len(prefix_as_n_gram)):
        text += " " + prefix_as_n_gram[i]
    return text[1:]


# for test purpose
if __name__ == "__main__":
    model = train_word_lm(PATH_FOR_TEST, n=10, smooth=True)
    created_text1 = generate(model, PATH_FOR_TEST)
    created_text2 = generate(model, PATH_FOR_TEST2)
    print(created_text1)
    print(created_text2)
