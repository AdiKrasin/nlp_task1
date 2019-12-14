from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.gather_statistic_handler import GatherStatisticHandler

DATA_SET_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set_unpacked"
files = ["ptb.test.txt", "ptb.train.txt", "ptb.valid.txt"]

if __name__ == "__main__":
    GD = GatherDataHandler(DATA_SET_PATH, UNPACK_PATH)
    GD.extract_all()
    GS = GatherStatisticHandler()
    # TODO CHECK IF N IS SOMETHING I NEED TO GET AS USER INPUT
    N = input("Please provide me with a number as input: ")
    result = GS.run(files, int(N))
    print("\nthese are the results:\n {}\n".format(result))
    GD.clean()
