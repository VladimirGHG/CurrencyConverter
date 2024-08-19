from django.shortcuts import render

from .forms import EnterCurrencies
from .scrap_cur_data import GoogleFinanceParser


def home_view(request):
    if request.method == 'POST':
        form = EnterCurrencies(request.POST)
        if form.is_valid():
            currency1 = form.cleaned_data['currency1']
            currency2 = form.cleaned_data['currency2']
            amount = form.cleaned_data['amount']

            return render(request, 'main_converter.html',
                          {'amount': amount, 'currency1': currency1, 'currency2': currency2,
                           "scrapData": GoogleFinanceParser})
    else:
        form = EnterCurrencies()
    return render(request, 'main_converter.html', {'form': form})
