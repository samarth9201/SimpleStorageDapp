pragma solidity >= 0.4.0 < 0.7.0;

contract Greeter{
    
    string public greeting;
    
    constructor() public {
        greeting = "Hello";
    }
    
    function setTransaction(string memory _greeting) public {
        greeting = _greeting;
    }
    
    function Greet() public view returns(string memory){
        return greeting;
    }
}