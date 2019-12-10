import string


class DataCleanerHandler:

    def __init__(self, tenk_most_frequent_words, tokens):
        self.tenk_most_frequent_words = [word.lower() for word in tenk_most_frequent_words]
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
        # TODO NEED TO REMOVE THE SPACE_ IN THE END OF EACH LINE: i think letter might be only \ and then only n
        for letter in clean_data:
            if letter == "\n":
                clean_data_to_return = clean_data_to_return + "\n"
            elif letter == " ":
                clean_data_to_return = clean_data_to_return + " _ "
            else:
                clean_data_to_return = clean_data_to_return + letter + " "
        clean_data_to_return = clean_data_to_return[:-1]
        return clean_data_to_return
