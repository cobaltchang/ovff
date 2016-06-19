from django.shortcuts import render

from ovff.forms import OvffForm
from ovff.models import Radicals

# Create your views here.


def home(request):
    ovff_form = OvffForm()
    result = []

    if request.method == 'POST':
        result = Radicals(request.POST)

    return render(request, 'ovff/home.html', {'form': ovff_form, 'radicals': result})