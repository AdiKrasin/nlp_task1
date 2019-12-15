from nltk.tokenize import RegexpTokenizer
import collections


class GatherStatisticHandler:

    def __init__(self, unpacked_path):
        self.tokenizer = RegexpTokenizer(r'\'*\w+\'*')
        self.result = dict()
        self.types_in_dev_data = dict()
        self.types_in_training_data = dict()
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
                content = file.read().replace('\n', '')
                # TODO CHECK IF THE TESTS ARE FRONTAL BECAUSE IT'S NOT CLEAR WHAT SHOULD BE THE OUTPUT'S STRUCTURE HERE
                tokens = self.tokenizer.tokenize(content)
                self.result['total_number_of_tokens '+file_name] = len(tokens)
                self.result['total_number_of_characters '+file_name] = len(content)
                # TODO CHECK WITH ELHADAD HOW IS IT POSSIBLE HERE THAT THE INPUT FILE IS ALREADY PROCESSED,
                #  MEANING EVERY WORD THAT IS NOT A PART OF THE 10K MOST FREQUENT WORD IS ALREADY <unk> AND EVERY
                #  NUMBER IS ALREADY N
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
                # TODO NEED TO CHECK WHAT DOES IT MEAN
                # TODO NEED TO CALCULATE THIS NOW: The average number and standard deviation of characters per token
                n_gram_value = [2, 3, 4]
                for value in n_gram_value:
                    n_grams = set()
                    split_content = content.split()
                    for index in range(len(split_content)-(value-1)):
                        element = ()
                        for index2 in range(value):
                            element = element + (split_content[index+index2],)
                        n_grams.add(element)
                    self.result['total_number_of_distinct_n_grams_of_words ' + str(value) + " " + file_name] = \
                        len(n_grams)
                n_gram_value = [2, 3, 4, 5, 6, 7]
                for value in n_gram_value:
                    n_grams = set()
                    for index in range(len(content)-(value-1)):
                        element = ""
                        for index2 in range(value):
                            element = element + content[index+index2]
                        n_grams.add(element)
                    self.result['total_number_of_distinct_n_grams_of_characters ' + str(value) + " " + file_name] = \
                        len(n_grams)
        return self.result
