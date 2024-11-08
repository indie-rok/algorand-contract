import typing as t
from algopy import ARC4Contract, String, Box, arc4, op, Contract,UInt64, subroutine,Txn, OnCompleteAction
from algopy.arc4 import abimethod
class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        self.box = Box(String)


    @abimethod()
    def hello(self, name: String) -> String:
        response = "Hello, " + name
        self.box.value = response
        return response

        
