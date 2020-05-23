from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contract
from web3 import Web3


# Create your views here.

class HomeView(TemplateView):
    template_name = 'Dapp/home.html'


    def post(self, request):
        web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        greeting = request.POST.get("Greet")
        contract = Contract.objects.filter(name="greeter.sol")[0]

        return render(request, "Dapp/home.html", context={
            'value': type(contract.abi)
        })
