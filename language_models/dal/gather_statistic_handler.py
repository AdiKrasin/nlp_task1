from nltk.tokenize import RegexpTokenizer
import collections

DATA_FOLDER_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set_unpacked\\simple-examples\\data\\"


class GatherStatisticHandler:

    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\'*\w+\'*')

    def run(self, file_name):
        result = dict()
        with open(DATA_FOLDER_PATH+file_name, "r") as content:
            # TODO WRITE THIS - COMPUTE ALL STAGE AND RETURN THE RESULT WITHIN THE RESULT DICT
            tokens = self.tokenizer.tokenize(content)
            result['total_number_of_tokens'] = len(tokens)
            result['total_number_of_charecters'] = len(content)
            result['total_number_of_distinct_words'] = len(collections.Counter(content))


