from language_models.main121 import train_word_lm
import os

cwd = os.getcwd()
PATH_FOR_TEST = cwd + "\\dal\\test.txt"
PATH_FOR_TEST2 = cwd + "\\dal\\test2.txt"


# for testing purpose
if __name__ == '__main__':
    actual_model = train_word_lm(PATH_FOR_TEST, n=3)
    perplexity_res1, infinity1 = actual_model.measure_perplexity(PATH_FOR_TEST)
    perplexity_res2, infinity2 = actual_model.measure_perplexity(PATH_FOR_TEST2)
    if not infinity1:
        print(perplexity_res1)
    else:
        print("infinity")
    if not infinity2:
        print(perplexity_res2)
    else:
        print("infinity")
    actual_model = train_word_lm(PATH_FOR_TEST, n=3, smooth=True)
    perplexity_res3 = actual_model.measure_perplexity(PATH_FOR_TEST)
    perplexity_res4 = actual_model.measure_perplexity(PATH_FOR_TEST2)
    print(perplexity_res3)
    print(perplexity_res4)
