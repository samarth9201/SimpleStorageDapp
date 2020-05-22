import json
from web3 import Web3
from solc import compile_files

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
compiled_sol = compile_files(['./contracts/greeter.sol'], output_values="")

class loadContract:
    
    
    
    def __init__(self):
        
        self.val = web3.isConnected()

    def isConnected(self):

        return self.val