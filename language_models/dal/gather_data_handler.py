from shutil import unpack_archive, rmtree
from urllib import request
from nltk.tokenize import RegexpTokenizer
import collections
import justext


def clean_html(html, language):
    paragraphs = justext.justext(html, justext.get_stoplist(language))
    return "\n".join([p.text for p in paragraphs if not p.is_boilerplate])


class GatherDataHandler:

    def __init__(self, top, url=None):
        self.top = top
        self.is_url = False
        if url is not None:
            self.url = url
            input_ans = input("is this a url? Y/N\n")
            if input_ans == "Y":
                self.is_url = True
                response = request.urlopen(self.url)
                self.raw = response.read().decode('utf-8')
                input_ans = input("what is the language of the content?\n")
                self.raw = clean_html(self.raw, input_ans)
            else:
                with open(url, 'r') as f:
                    self.raw = f.read()
            self.tokenizer = RegexpTokenizer(r'\'*\w+\'*')
            self.raw = self.raw.replace("\n", " backslashn ")
            self.tokens = self.tokenizer.tokenize(self.raw)

    def extract_all(self):
        unpack_archive(self.path_to_data_set, self.path_to_unpack)

    def run(self):
        counter = collections.Counter(self.raw.split())
        tenk_most_frequent_words = counter.most_common(self.top+1)
        return tenk_most_frequent_words, self.tokens, self.is_url

    def clean(self):
        rmtree(self.path_to_unpack, ignore_errors=True)
