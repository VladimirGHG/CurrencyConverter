from django import forms


class EnterCurrencies(forms.Form):
    currency1 = forms.CharField(max_length=10, initial="USD")
    currency2 = forms.CharField(max_length=10, initial="EUR")
    amount = forms.IntegerField()
