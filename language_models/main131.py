from language_models.main121 import train_word_lm
import os
from language_models.dal.gather_data_handler import GatherDataHandler
import matplotlib.pyplot as plt

cwd = os.getcwd()

DATA_SET_PATH = cwd + "\\dal\\data_set\\simple-examples.tgz"
UNPACK_PATH = cwd + "\\dal\\data_set_unpacked"


# for testing purpose
if __name__ == '__main__':
    ns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    values = []
    for n in ns:
        GD = GatherDataHandler(10000, path_to_data_set=DATA_SET_PATH, path_to_unpack=UNPACK_PATH)
        GD.extract_all()
        actual_model = train_word_lm(UNPACK_PATH + "\\simple-examples\\data\\ptb.train.txt", n=n, smooth=True,
                                     gamma=0.9)
        perplexity_res = actual_model.measure_perplexity(UNPACK_PATH + "\\simple-examples\\data\\ptb.valid.txt")
        GD.clean()
        values.append(perplexity_res)
        print(str(perplexity_res)+"\n")
    plt.plot(values, ns, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue',
             markersize=12)
    plt.ylabel('ns')
    plt.xlabel('perplexity')
    plt.ylim = 20
    plt.xlim = 95
    plt.show()
