from ovff.models import Radical


def regen_database():
    Radical.objects.all().delete()
    with open('boshiamy.dat', 'r') as f:
        for line in f.readlines():
            radical, word = line.split(' ')
            word = word.rstrip('\n')
            record = Radical(radical=radical, word=word)
            record.full_clean()
            record.save()
