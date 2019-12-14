from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.gather_statistic_handler import GatherStatisticHandler
import os

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = cwd + "\\dal\\data_set_unpacked"
files = ["ptb.test.txt", "ptb.train.txt", "ptb.valid.txt"]

if __name__ == "__main__":
    GD = GatherDataHandler(DATA_SET_PATH, UNPACK_PATH)
    GD.extract_all()
    GS = GatherStatisticHandler(UNPACK_PATH)
    # TODO CHECK IF N IS SOMETHING I NEED TO GET AS USER INPUT
    # TODO CREATE A NOTEBOOK
    N = input("Please provide me with a number as input: ")
    result = GS.run(files, int(N))
    print("\nthese are the results:\n {}\n".format(result))
    GD.clean()
