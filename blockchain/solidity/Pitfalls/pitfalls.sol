pragma solidity ^0.4.0;

// RE-ENTRANCY
contract Fund
{
    // Mapping of ether shares of the contract
    mapping(address => uint) shares;
    // Withdraw your share 
    function withdraw() public 
    {
        if (msg.sender.send(shares[msg.sender]))
            shares[msg.sender] = 0;
    }
}
