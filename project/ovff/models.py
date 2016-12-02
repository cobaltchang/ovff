import os

# Create your models here.


class Radicals:
    radicals = []

    def __init__(self, post):
        self.query = post['query']
        if self.query:
            self.radicals = self.query_radicals(self.query)

    def query_radicals(self, query):
        radicals = []

        cwd = os.path.dirname(__file__)
        radicals_file = os.path.dirname(cwd) + '/misc/boshiamy.dat'
        with open(radicals_file, 'r', encoding='utf-8') as fp:
            for line in fp:
                if query in line:
                    radicals += [tuple(line.split()), ]

        return radicals
