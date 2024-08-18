from django.shortcuts import render

from .forms import EnterCurrencies


def home_view(request):
    context = {'form': EnterCurrencies()}
    return render(request, "amin_converter.html", context)
