from django.db import models

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


class Radical(models.Model):
    radical = models.CharField(max_length=5)
    word = models.CharField(max_length=1)

    def __str__(self):
        return self.word
