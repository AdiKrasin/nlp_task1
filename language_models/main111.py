# import nltk
from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.data_cleaner_handler import DataCleanerHandler
import os

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = cwd + "\\dal\\data_set_unpacked"


def ptb_preprocess(filenames, top=10000):
    # downloaded the nltk_data folder to a central location with this line: (ran it once)
    # nltk.download()
    # TODO MAYBE INSTEAD OF URL IT SHOULD BE FILENAMES
    url = input("Please provide me with a url as input: ")
    # TODO CHECK ALL OF THIS WITH ELHADAD (SUNDAY CLASS):
    # 1. TODO NEED TO WRITE THIS FUNCTION THAT WILL RAP ALL LO OF THE CODE: ptb_preprocess(filenames, top=10000) SO I
    #       NEED TO UNDERSTAND WHAT IS THE FILE NAME BECAUSE BEFORE IT WAS WRITTEN TAKE AN INPUT URL.
    # 2. TODO CAN I ASSUME THAT THE CONTENT IS HTML? IF IT IS I WANT TO CLEAN THE TAGS WITH BS4 PRIOR TO THE STAGES
    # 3. TODO WHAT IS GOING ON WITH THE DATA SET? IS THE DATA SET SUPPOSED TO BE THE DATA SET I DOWNLOADED OR IS IT
    #       THE URL'S CONTENT ITSELF OR BROWN'S DATA SET FROM NLTK?
    # 4. TODO IN THE END WRITE THE NOTEBOOK
    GD = GatherDataHandler(DATA_SET_PATH, UNPACK_PATH, top, url)
    tenk_most_frequent_words, tokens = GD.run()
    DC = DataCleanerHandler(tenk_most_frequent_words, tokens)
    clean_data = DC.run()
    # TODO DELETE THE PRINT WHEN FINISH TESTING
    print(clean_data)


# TODO DELETE THIS WHEN FINISH TESTING
if __name__ == "__main__":
    ptb_preprocess("")
