from django.shortcuts import render
from django.db.models import Q

from ovff.forms import OvffForm
from ovff.models import Radical


# Create your views here.


def home(request):
    ovff_form = OvffForm()
    result = {}

    if request.method == 'POST':
        queryset = Radical.objects.filter(Q(radical__contains=request.POST['query']) |
                                          Q(word__contains=request.POST['query']))
        result['radicals'] = [(query.radical, query.word) for query in queryset]

    return render(request, 'ovff/home.html', {'form': ovff_form, 'radicals': result})
