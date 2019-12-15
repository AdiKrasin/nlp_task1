import string


class DataCleanerHandler:

    def __init__(self, tenk_most_frequent_words, tokens):
        self.tenk_most_frequent_words = [word[0].lower() for word in tenk_most_frequent_words]
        if "backslashn" not in self.tenk_most_frequent_words:
            self.tenk_most_frequent_words = self.tenk_most_frequent_words[:-1]
        self.tokens = tokens
        self.raw = [word.lower() for word in self.tokens if word not in string.punctuation]

    def run(self):
        index = 0
        for word in self.raw:
            if word not in self.tenk_most_frequent_words and not word.isdigit() and word != "backslashn":
                self.raw[index] = "<unk>"
            if word.isdigit():
                self.raw[index] = "N"
            index = index + 1
        clean_data = ""
        for word in self.raw:
            if word == "backslashn":
                clean_data = clean_data + "\n"
            else:
                clean_data = clean_data + word + " "
        clean_data = clean_data[:-1]
        clean_data_to_return = ""
        for letter in clean_data:
            if letter == "\n":
                clean_data_to_return = clean_data_to_return[:-3] + "\n"
            elif letter == " ":
                clean_data_to_return = clean_data_to_return + "_ "
            else:
                clean_data_to_return = clean_data_to_return + letter + " "
        clean_data_to_return = clean_data_to_return[:-1]
        return clean_data_to_return
