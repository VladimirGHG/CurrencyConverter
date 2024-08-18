from django import forms


class EnterCurrencies(forms.Form):
    currency1 = forms.CharField(max_length=10)
    currency2 = forms.CharField(max_length=10)
    amount = forms.IntegerField(help_text="Enter only Positive Integers")
