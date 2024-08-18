from django.shortcuts import render

from .forms import EnterCurrencies


def home_view(request):
    context = {'form': EnterCurrencies()}
    return render(request, "main_converter.html", context)
