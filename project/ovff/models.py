# Create your models here.


class Radicals:
    def __init__(self, query):
        self.word = query['word']
        self.radicals = self.query_radicals(self.word)

    def query_radicals(self, word):
        radicals = []

        # TODO: query it
        radicals += ['ovff']

        return radicals
