from shutil import unpack_archive, rmtree
from urllib import request
from nltk import word_tokenize


class GatherDataHandler:

    def __init__(self, path_to_data_set, path_to_unpack, url):
        self.path_to_data_set = path_to_data_set
        self.path_to_unpack = path_to_unpack
        self.url = url
        response = request.urlopen(self.url)
        self.raw = response.read().decode('utf-8')
        self.tokens = word_tokenize(self.raw)

    def extract_all(self):
        unpack_archive(self.path_to_data_set, self.path_to_unpack)

    def run(self):
        self.extract_all()
        self.clean()
        # TODO SHOULD RETURN THE 10K MOST FREQUENT WORDS
        return [], self.tokens

    def clean(self):
        rmtree(self.path_to_unpack, ignore_errors=True)


