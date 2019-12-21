from nltk.tokenize import RegexpTokenizer
import collections
import math


class GatherStatisticHandler:

    def __init__(self, unpacked_path, cooking=False):
        self.tokenizer = RegexpTokenizer(r'\'*\w+\'*')
        self.result = dict()
        self.types_in_dev_data = dict()
        self.types_in_training_data = dict()
        if cooking:
            self.data_folder_path = unpacked_path+"\\"
        else:
            self.data_folder_path = unpacked_path + "\\simple-examples\\data\\"

    def calc_number_of_types_in_dev_not_in_train(self):
        counter = 0
        for word in set(list(self.types_in_dev_data.elements())):
            if word not in self.types_in_training_data:
                counter += self.types_in_dev_data[word]
            elif self.types_in_dev_data[word] > self.types_in_training_data[word]:
                counter += self.types_in_dev_data[word] - self.types_in_training_data[word]
        return counter

    def run(self, files, n):
        for file_name in files:
            with open(self.data_folder_path+file_name, "r") as file:
                content_as_string = file.read().replace('\n', '')
                content = content_as_string.split()
                tokens = self.tokenizer.tokenize(content_as_string)
                self.result['total_number_of_tokens '+file_name] = len(tokens)
                self.result['total_number_of_characters '+file_name] = len(content_as_string)
                self.result['total_number_of_distinct_words '+file_name] = \
                    len(set(list(collections.Counter(content).elements())))
                collection_without_unk_and_n = collections.Counter(content)
                del collection_without_unk_and_n["N"]
                del collection_without_unk_and_n["<unk>"]
                if file_name == "ptb.test.txt":
                    self.types_in_dev_data = collection_without_unk_and_n
                elif file_name == "ptb.train.txt":
                    self.types_in_training_data = collection_without_unk_and_n
                most_common_n = collection_without_unk_and_n.most_common(n)
                self.result['total_number_of_token_top_N_most_frequent '+file_name] = 0
                for token in tokens:
                    if token in most_common_n:
                        self.result['total_number_of_token_top_N_most_frequent '+file_name] += 1
                self.result['token_type_ratio '+file_name] = self.result['total_number_of_tokens '+file_name] / \
                    self.result['total_number_of_distinct_words '+file_name]
                if self.types_in_training_data and self.types_in_dev_data:
                    self.result['number_of_types_in_dev_not_in_train'] = self.calc_number_of_types_in_dev_not_in_train()
                number_of_chars = 0
                for token in tokens:
                    number_of_chars += len(token)
                self.result['average_number_of_characters_per_token '+file_name] = number_of_chars / len(tokens)
                numbers_of_chars_manipulation = []
                for token in tokens:
                    numbers_of_chars_manipulation.append(math.pow(len(token)-self.result['average_number_of_characters_per_token '+file_name], 2))
                number_of_chars = 0
                for number in numbers_of_chars_manipulation:
                    number_of_chars += number
                self.result['standard_deviation_of_characters_per_token '+file_name] = math.sqrt(number_of_chars /
                                                                                                 len(tokens))
                n_gram_value = [2, 3, 4]
                for value in n_gram_value:
                    n_grams = set()
                    for index in range(len(content)-(value-1)):
                        element = ()
                        for index2 in range(value):
                            element = element + (content[index+index2],)
                        n_grams.add(element)
                    self.result['total_number_of_distinct_n_grams_of_words ' + str(value) + " " + file_name] = \
                        len(n_grams)
                n_gram_value = [2, 3, 4, 5, 6, 7]
                for value in n_gram_value:
                    n_grams = set()
                    for index in range(len(content_as_string)-(value-1)):
                        element = ""
                        for index2 in range(value):
                            element = element + content_as_string[index+index2]
                        n_grams.add(element)
                    self.result['total_number_of_distinct_n_grams_of_characters ' + str(value) + " " + file_name] = \
                        len(n_grams)
        return self.result
