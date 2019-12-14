from language_models.models.ngram_model import NgramModel


def train_word_lm(data_set, n=2):
    # TODO NEED TO MAKE SURE THE DATA SET IS BEING SENT AS STRING
    my_model = NgramModel(data_set, n)
    my_model.run()
    # TODO DELETE THIS WHEN FINISH TESTING
    print(my_model.model[('adi',)]['kk'])
    return


# TODO REMOVE IT WHEN FINISH TESTING
if __name__ == "__main__":
    train_word_lm("adi krasin is the most amazing person in the world adi kk")
