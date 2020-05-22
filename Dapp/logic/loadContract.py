import json
import os
import json
from web3 import Web3
from solc import compile_files

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

### Get absolute path of logic
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

### Get absolute path of contracts directory
CONTRACT_DIR = os.path.join(BASE_DIR, 'logic/contracts/')

### Compiling Contract
contract = compile_files([CONTRACT_DIR + "greeter.sol"],
                         output_values=["abi,asm,ast,bin,bin-runtime,devdoc,interface,opcodes,userdoc"])

### Getting compiled json(python-dict) for greeter contract
greeter = contract[CONTRACT_DIR + "greeter.sol" + ":Greeter"]

### Getting abi and bytecode of Contract

abi = greeter['abi']
bytecode = greeter['bin']

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)
web3.eth.defaultAccount = web3.eth.accounts[0]
tx_hash = web3.toHex(Greeter.constructor().transact())