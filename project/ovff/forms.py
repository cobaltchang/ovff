from django import forms


class OvffForm(forms.Form):
    query = forms.CharField(label='請輸入您要查詢的拆碼或文字')
