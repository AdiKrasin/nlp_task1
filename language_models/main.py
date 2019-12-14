# import nltk
from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.data_cleaner_handler import DataCleanerHandler

DATA_SET_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set_unpacked"

# TODO CREATE THIS IN THE REQUESTED NAMES

if __name__ == "__main__":
    # downloaded the nltk_data folder to a central location with this line: (ran it once)
    # nltk.download()
    url = input("Please provide me with a url as input: ")
    # TODO CHECK ALL OF THIS WITH ELHADAD (SUNDAY CLASS):
    # 1. TODO NEED TO WRITE THIS FUNCTION THAT WILL RAP ALL LO OF THE CODE: ptb_preprocess(filenames, top=10000) SO I
    #       NEED TO UNDERSTAND WHAT IS THE FILE NAME BECAUSE BEFORE IT WAS WRITTEN TAKE AN INPUT URL.
    # 2. TODO CAN I ASSUME THAT THE CONTENT IS HTML? IF IT IS I WANT TO CLEAN THE TAGS WITH BS4 PRIOR TO THE STAGES
    # 3. TODO WHAT IS GOING ON WITH THE DATA SET? IS THE DATA SET SUPPOSED TO BE THE DATA SET I DOWNLOADED OR IS IT
    #       THE URL'S CONTENT ITSELF OR BROWN'S DATA SET FROM NLTK?
    # 4. TODO IN THE END WRITE THE NOTEBOOK
    GD = GatherDataHandler(DATA_SET_PATH, UNPACK_PATH, url)
    tenk_most_frequent_words, tokens = GD.run()
    DC = DataCleanerHandler(tenk_most_frequent_words, tokens)
    clean_data = DC.run()
    # TODO DELETE THE PRINT WHEN FINISH TESTING
    print(clean_data)



