from django.shortcuts import render
from django.http import HttpResponse
from .logic import loadContract

# Create your views here.
def home(request):
    value = loadContract.tx_hash
    context = {
        'value': value,
        }
    return render(request, "Dapp/home.html", context)

def index(request):
    return HttpResponse("Hello, inside Dapp")