from language_models.dal.gather_data_handler import GatherDataHandler
from language_models.dal.gather_statistic_handler import GatherStatisticHandler
import os
import json

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = cwd + "\\dal\\data_set_unpacked"
files = ["ptb.test.txt", "ptb.train.txt", "ptb.valid.txt"]

if __name__ == "__main__":
    GD = GatherDataHandler(10000, path_to_data_set=DATA_SET_PATH, path_to_unpack=UNPACK_PATH)
    GD.extract_all()
    GS = GatherStatisticHandler(UNPACK_PATH)
    N = input("Please provide me with a number as input: ")
    result = GS.run(files, int(N))
    print("\nthese are the results:\n {}\n".format(json.dumps(result, indent=4)))
    GD.clean()
