from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "Dapp/home.html")

def index(request):
    return HttpResponse("Hello, inside Dapp")