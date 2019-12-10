from shutil import unpack_archive, rmtree
from urllib import request
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!')


class GatherDataHandler:

    def __init__(self, path_to_data_set, path_to_unpack, url):
        self.path_to_data_set = path_to_data_set
        self.path_to_unpack = path_to_unpack
        self.url = url
        response = request.urlopen(self.url)
        self.raw = response.read().decode('utf-8')
        # TODO DELETE THIS AFTER TESTING
        self.raw = """consumers may want to move their telephones a little closer to the tv set
adi adi watching abc 's monday night football can now vote during <unk> for the greatest play in 100 years
from among four or five! ! adi adi """
        self.tokenizer = RegexpTokenizer(r'\'*\w+\'*')
        # TODO THIS IS A RISKY WAY TO DO SO BECAUSE THE WORD backslashn MAY APPEAR AND THEN I SHOULD NOT TURN IT INTO \n
        self.raw = self.raw.replace("\n", " backslashn ")
        self.tokens = self.tokenizer.tokenize(self.raw)

    def extract_all(self):
        unpack_archive(self.path_to_data_set, self.path_to_unpack)

    def run(self):
        self.extract_all()
        tenk_most_frequent_words = dict()
        # TODO DELETE THIS AFTER TESTING:
        tenk_most_frequent_words = {'consumers': 1, 'may': 1, 'want': 1, 'to': 1, 'move': 1, 'their': 1,
                                    'telephones': 1, 'a': 1, 'little': 1, 'closer': 1, 'to': 1, 'the': 1, 'tv': 1,
                                    'set': 1, 'watching': 1, 'abc': 1, '\'s': 1, 'monday': 1, 'night': 1, 'football': 1,
                                    'can': 1, 'now': 1, 'vote': 1, 'during': 1, 'for': 1, 'greatest': 1, 'play': 1,
                                    'in': 1, 'years': 1, 'from': 1, 'among': 1, 'four': 1, 'or': 1, 'five': 1}
        # TODO SHOULD CALCULATE THE 10K MOST FREQUENT WORDS
        self.clean()
        return tenk_most_frequent_words, self.tokens

    def clean(self):
        rmtree(self.path_to_unpack, ignore_errors=True)


