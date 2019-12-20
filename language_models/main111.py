# import nltk
from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.data_cleaner_handler import DataCleanerHandler


def ptb_preprocess(filenames, top=10000):
    # downloaded the nltk_data folder to a central location with this line: (ran it once)
    # nltk.download()
    for file_name in filenames:
        GD = GatherDataHandler(top, file_name)
        tenk_most_frequent_words, tokens, is_url = GD.run()
        DC = DataCleanerHandler(tenk_most_frequent_words, tokens)
        clean_data = DC.run()
        if not is_url:
            with open(file_name+".out", "w+") as f:
                f.write(clean_data)
        else:
            print("\n\n\n\n\n\n")
            print('the output for the following file: {}'.format(file_name))
            print(clean_data)


# for testing purpose
if __name__ == "__main__":
    list_of_files = ['https://www.walla.co.il',
                     'https://www.cs.bgu.ac.il/~elhadad/nlp20/hw1.html',
                     'https://cs.stanford.edu/people/karpathy/char-rnn/shakespeare_input.txt']
    ptb_preprocess(list_of_files)
