import codecs
import math
import random
import string
import time
import numpy as np
#import torch
#from sklearn.metrics import accuracy_score
import unicodedata
import os


'''
Don't change these constants for the classification task.
You may use different copies for the sentence generation model.
'''
languages = ["af", "cn", "de", "fi", "fr", "in", "ir", "pk", "za"]
all_letters = string.ascii_letters + " .,;'"


# Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

# print(unicodeToAscii('Ślusàrski'))

# Build the category_lines dictionary, a list of names per language
category_lines = {}
all_categories = []


# Read a file and split into lines
def readLines(filename):
    lines = codecs.open(filename,  "r", encoding='utf-8', errors='ignore').read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]


if __name__ == '__main__':
    file_names = ['C:\\Users\\adikr\\Desktop\\nlp_task1\\data\\cities\\train\\cities_train\\train\\' + file_name for
                  file_name in
                  os.listdir('C:\\Users\\adikr\\Desktop\\nlp_task1\\data\\cities\\train\\cities_train\\train')]

    print('number of categories is:'
          ' {}\n'.format(len(os.listdir('C:\\Users\\adikr\\Desktop\\nlp_task1\\data\\cities\\train\\cities_train\\train'))))

    for file_name in file_names:
        result = readLines(file_name)

        print('statistics for the following file: {}\n'.format(file_name))
        print('token per category: {}\n'.format(len(result)))
        print('number of chars is: {}\n'.format(np.sum([len(word) for word in result])))
        distinct_chars = list()
        for word in result:
            for letter in word:
                if letter not in distinct_chars:
                    distinct_chars.append(letter)
        print('number of distinct chars is: {}\n'.format(len(distinct_chars)))
        print('average number of chars per token is: {}\n'.format(np.mean([len(word) for word in result])))
