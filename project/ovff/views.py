from django import forms
from django.shortcuts import render

from ovff.models import Radicals


# Create your views here.


class OvffForm(forms.Form):
    query = forms.CharField(label='請輸入您要查詢的拆碼或文字')


def home(request):
    ovff_form = OvffForm()
    result = []

    if request.method == 'POST':
        result = Radicals(request.POST)

    return render(request, 'ovff/home.html', {'form': ovff_form, 'radicals': result})