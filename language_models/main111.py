# import nltk
from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.data_cleaner_handler import DataCleanerHandler


def ptb_preprocess(filenames, top=10000):
    # downloaded the nltk_data folder to a central location with this line: (ran it once)
    # nltk.download()
    GD = GatherDataHandler(top, filenames)
    tenk_most_frequent_words, tokens, is_url = GD.run()
    DC = DataCleanerHandler(tenk_most_frequent_words, tokens)
    clean_data = DC.run()
    if not is_url:
        with open(filenames+".out", "w+") as f:
            f.write(clean_data)


# for testing purpose
if __name__ == "__main__":
    #ptb_preprocess('https://www.cs.bgu.ac.il/~elhadad/nlp20/hw1.html')
    ptb_preprocess('C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\test.txt', top=2)
