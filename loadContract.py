import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'SimpleStorageDapp.settings')
django.setup()
import json
from web3 import Web3
from solc import compile_files
from Dapp.models import Contract

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
for c in Contract.objects.all():
    c.delete()


class DeployContract:

    def __init__(self, contract_name):

        ### Get absolute path of contracts
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        ### Get absolute path of contracts directory
        CONTRACT_DIR = os.path.join(BASE_DIR, 'SimpleStorageDapp/contracts/contracts/')

        ### Compiling Contract
        contract = compile_files([CONTRACT_DIR + f"{contract_name}"],
                                 output_values=["abi,asm,ast,bin,bin-runtime,devdoc,interface,opcodes,userdoc"])

        ### Getting compiled json(python-dict) for greeter contract
        greeter = contract[CONTRACT_DIR + f"{contract_name}" + ":Greeter"]

        ### Getting abi and bytecode of Contract
        self.contract_name = contract_name
        self.abi = greeter['abi']
        self.bytecode = greeter['bin']

    def deployContract(self):

        Greeter = web3.eth.contract(abi=self.abi, bytecode=self.bytecode)
        web3.eth.defaultAccount = web3.eth.accounts[0]
        tx_hash = Greeter.constructor().transact()
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        Greeter = web3.eth.contract(address=tx_receipt.contractAddress, abi=self.abi)
        address = tx_receipt.contractAddress
        contract = web3.eth.contract(address=address, abi=self.abi)
        return address, self.abi, self.bytecode, self.contract_name, contract

contract = DeployContract('greeter.sol')
address, abi, bytecode, contract_name, contract = contract.deployContract()

c = Contract(name=contract_name, abi=abi, bytecode=bytecode, address=address, contract=contract)
c.save()