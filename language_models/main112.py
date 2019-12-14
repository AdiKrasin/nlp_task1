from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.gather_statistic_handler import GatherStatisticHandler

DATA_SET_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = "C:\\Users\\adikr\\Desktop\\nlp_task1\\language_models\\dal\\data_set_unpacked"
files = ["ptb.test.txt", "ptb.train.txt", "ptb.valid.txt"]

if __name__ == "__main__":
    GD = GatherDataHandler(DATA_SET_PATH, UNPACK_PATH)
    GD.extract_all()
    GS = GatherStatisticHandler()
    for file_name in files:
        result = GS.run(file_name)
        print("\nfor the following file name: {}\n these are the results:\n {}\n".format(file_name, result))
    GD.clean()
