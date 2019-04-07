'''
Author: Parker Folkman
Date: 4/24/2018
Overview: This is a Modified Proof of Stake blockchain that resolves
the lazy miner problem as well as the rich get richer problem. This code
was written as a programming assignment in CSCI 520 Distributed Systems at 
Montana State University. This code is free for anyone to use at your discretion. This software comes
As-Is with no warranties guaranteed or implied. 

Please see the Readme for the assignment prompt for the specifications that this code addresses. 

'''

import socket
import threading
import time
import datetime
import sys
import pickle
import json
from block import Block


def writeToLog(logEntry):
    file = open("log.txt", "a")
    #write the log out to a file
    file.write('\n')
    file.write(logEntry)
    file.close()

# block strings need to be of the form:
# "block;blockNum;trans|sender|receiver|amount;timestamp;signature1|signature2"
def parseBlock(block_str):
    blockValues = block_str.split(";")
    blockNum = blockValues[1]

    transaction_str = blockValues[2]
    trans_temp = transaction_str.split("|")
    sender = trans_temp[1]
    receiver = trans_temp[2]
    amount = trans_temp[3]
    trans_L = [sender,receiver,amount]

    timestamp = blockValues[3]

    signatures_str = blockValues[4]
    signatures_L = signatures_str.split("|")

    newblock = Block(blockNum,trans_L,timestamp,signatures_L)
    return newblock

def parseTransaction(transaction_str):
    values = transaction_str.split("|")
    sender = values[1]
    receiver = values[2]
    amount = values[3]
    transaction_L = [sender,receiver,amount]
    return transaction_L

def createTransaction():
    spender = input("Who is spending?: ")
    receiver = input("Who is receiving?: ")
    amount = input("What is the amount?: ")
    transaction = "trans|%s|%s|%s" % (spender,receiver,amount)
    return transaction

# return a value from 0-3 designating which node will create next block
def getTurn():
    return len(blockchain)%4

def blockToString(block):
    blockNum = block.blockNumber
    timestamp = block.timestamp
    trans_L = block.transactions
    trans_str = "trans|%s|%s|%s"%(trans_L[0],trans_L[1],trans_L[2])
    sigs_L = block.signatures
    sigs_str = ''
    count = 0
    for sig in sigs_L:
        count +=1
        sigs_str = sigs_str+sig
        if count != len(sigs_L):
            sigs_str = sigs_str+"|"
    blockString = "block;%s;%s;%s;%s"%(blockNum,trans_str,timestamp,sigs_str)
    return blockString

def serverThread():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if nodeName == 'node1':
        serversocket.bind((ip_dict.get('node1'), 5000))
    elif nodeName == 'node2':
        serversocket.bind((ip_dict.get('node2'), 5000))
    elif nodeName == 'node3':
        serversocket.bind((ip_dict.get('node3'), 5000))
    elif nodeName == 'node4':
        serversocket.bind((ip_dict.get('node4'), 5000))
    serversocket.listen(5)  # server socket maximum 5 connections

    global newBlock
    nodeTurn = ''

    while True:
        connection, address = serversocket.accept()
        buf = connection.recv(4096)

        currentTurn = getTurn()
        if currentTurn == 0:
            nodeTurn = 'node1'
        elif currentTurn == 1:
            nodeTurn = 'node2'
        elif currentTurn == 2:
            nodeTurn = 'node3'
        elif currentTurn == 3:
            nodeTurn = 'node4'

        if len(buf) > 0:
            msg = pickle.loads(buf)
            msgValues = msg.split(";")
            msgType = msgValues[0]
            msg_trans_type = msgType
            if len(msgType) > 9 and msgType != 'block':
                msgValues = msgType.split("|")
                msgType = msgValues[0]

            if msgType == 'ACK':
                print("ACK received %s" % (msg))
            elif msgType == 'prntChain':
                printBlockchain()
            elif msgType == 'prntLdg':
                printLedger()
            elif msgType == 'yes': #block was accepted
                thisNodeTurn = turn_dict.get(nodeName)
                currentTurn = getTurn()
                if thisNodeTurn == currentTurn:
                    prevBlock = blockchain[-1]
                    #Only add the block to the chain once
                    if prevBlock.blockNumber != newBlock.blockNumber:
                        blockchain.append(newBlock)
                        tmpBlockString = blockToString(newBlock)
                        writeToLog("  |  ")
                        writeToLog("  V  ")
                        writeToLog(tmpBlockString)
                        #Update the ledger
                        sender = newBlock.transactions[0]
                        receiver = newBlock.transactions[1]
                        amount = newBlock.transactions[2]
                        amount = int(amount)
                        ledger_dict[sender] -= amount
                        ledger_dict[receiver] += amount

            elif msgType == 'block':
                receivedBlock = parseBlock(msg)
                #check the block for double spending
                sender = receivedBlock.transactions[0]
                receiver = receivedBlock.transactions[1]
                amount = receivedBlock.transactions[2]
                amount = int(amount)
                senderBal = ledger_dict.get(sender)
                if amount <= senderBal:
                    # serverSendMsgToAll("yes")
                    myStake = stake_dict.get(nodeName)
                    myStake = int(myStake)
                    if amount < myStake:
                        print("Transaction approved with adequate stake")
                        receivedBlock.signBlock(nodeName)
                    else:
                        print("Transaction looks good, but I dont have enough stake.")
                        print("I will wait for the block to be sent back to me. ")
                    blockchain.append(receivedBlock)
                    tmpBlockString = blockToString(receivedBlock)
                    writeToLog("  |  ")
                    writeToLog("  V  ")
                    writeToLog(tmpBlockString)
                    #Update the ledger
                    ledger_dict[sender] -= amount
                    ledger_dict[receiver] += amount
                    #ledger_dict[nodeName] += 10 # reward for signing the block
                    if nodeTurn == 'node1' and nodeName != 'node1':
                        ledger_dict['node1'] += 30
                    elif nodeTurn == 'node2' and nodeName != 'node2':
                        ledger_dict['node2'] += 30
                    elif nodeTurn == 'node3' and nodeName != 'node3':
                        ledger_dict['node3'] += 30
                    elif nodeTurn == 'node4' and nodeName != 'node4':
                        ledger_dict['node4'] += 30
                else:
                    print("Double spending found. Voting NO")
                    serverSendMsgToAll("no")

            elif msgType == 'trans':
                trans_L = parseTransaction(msg_trans_type)
                sender = trans_L[0]
                receiver = trans_L[1]
                amount = trans_L[2]
                amount = int(amount)
                senderBal = ledger_dict.get(sender)

                thisNodeTurn = turn_dict.get(nodeName)
                currentTurn = getTurn()
                if thisNodeTurn == currentTurn:
                    print("My turn to create a block!")
                    if amount <= senderBal:
                        print("Transaction approved")
                        #create a block
                        previousBlock = blockchain[-1]
                        tmpBlockNum = int(previousBlock.blockNumber)
                        newBlockNumber = tmpBlockNum+1
                        signatures = []
                        newBlock = Block(newBlockNumber,
                                         trans_L,
                                         datetime.datetime.now(),
                                         signatures)
                        tempBlockList = [newBlock]
                        #Sign the block
                        newBlock.signBlock(nodeName)
                        ledger_dict[nodeName] +=10 #Reward for signing block
                        blockchain.append(newBlock)
                        tmpBlockString = blockToString(newBlock)
                        writeToLog("  |  ")
                        writeToLog("  V  ")
                        writeToLog(tmpBlockString)
                        ledger_dict[sender] -= amount
                        ledger_dict[receiver] += amount
                        ledger_dict[nodeName] += 20 # Reward for creating block
                        blockString = blockToString(newBlock)
                        print(blockString)
                        serverSendMsgToAll(blockString)
                    else:
                        print("Double Spending event found. Transaction will not be processed.")

            else:
                print("Read [%s] from buffer" % (msg))
                #check if its a good transaction
                # if its a bad transaction do nothing
                # if its a good transaction, create a block > sign block
                    # a. create a block
                    # b. sign the block
                    # c. prepare the block for sending
                    # d. send the block to the other nodes
                serverSendMsgToAll("ACK")
# End Server thread

# def prepareBlock(block):
#

def serverSendMsgToAll(msg):
    clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if nodeName == 'node1':
        clientsocket1.connect((ip_dict.get('node2'), 5000))
        clientsocket2.connect((ip_dict.get('node3'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node2':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node3'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node3':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node2'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node4':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node2'), 5000))
        clientsocket3.connect((ip_dict.get('node3'), 5000))

    p = pickle.dumps(msg)
    clientsocket1.send(p)
    clientsocket2.send(p)
    clientsocket3.send(p)

def clientSendToAll(transaction):
    clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clientsocket1.connect((ip_dict.get('node1'), 5000))
    clientsocket2.connect((ip_dict.get('node2'), 5000))
    clientsocket3.connect((ip_dict.get('node3'), 5000))
    clientsocket4.connect((ip_dict.get('node4'), 5000))

    p = pickle.dumps(transaction)
    clientsocket1.send(p)
    clientsocket2.send(p)
    clientsocket3.send(p)
    clientsocket4.send(p)

#Client Thread
def clientThread():
    clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if nodeName == 'node1':
        clientsocket1.connect((ip_dict.get('node2'), 5000))
        clientsocket2.connect((ip_dict.get('node3'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node2':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node3'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node3':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node2'), 5000))
        clientsocket3.connect((ip_dict.get('node4'), 5000))
    elif nodeName == 'node4':
        clientsocket1.connect((ip_dict.get('node1'), 5000))
        clientsocket2.connect((ip_dict.get('node2'), 5000))
        clientsocket3.connect((ip_dict.get('node3'), 5000))

def printBlockchain():
    print()
    count = 0
    blockchain_length = len(blockchain)
    for block in blockchain:
        count += 1
        print("***************************************")
        print("Block Number: %s" % (block.blockNumber))
        print("Block Transactions: %s" % (block.transactions))
        print("Block Timestamp: %s" % (block.timestamp))
        print("Block Signatures: %s" % (block.signatures))
        print("***************************************")
        if count != blockchain_length:
            print("     |     ")
            print("     |     ")
            print("     V     ")
    print()

def printLedger():
    print(json.dumps(ledger_dict, indent=1))

if __name__ == "__main__":
    threads = []
    nodeName = sys.argv[1]

    ip_dict = {
        'node1': '10.142.0.10',
        'node2': '10.142.0.11',
        'node3': '10.142.0.12',
        'node4': '10.142.0.13',
    }

    ledger_dict = {
        'node1': 0,
        'node2': 0,
        'node3': 0,
        'node4': 0,
        'Parker': 100,
        'Mike': 100,
        'Jeff': 100,
        'Bentley': 100,
        'Alice': 100,
        'Bob': 100
    }

    stake_dict = {
        'node1': 10,
        'node2': 20,
        'node3': 50,
        'node4': 80
    }

    turn_dict = {
        'node1': 0,
        'node2': 1,
        'node3': 2,
        'node4': 3
    }

    #make sure the log is clear.
    with open('log.txt', 'w'):
        pass

    init_transactions = []
    init_signatures = []
    genesisBlock = Block(0, init_transactions,
                         datetime.datetime.now(),
                         init_signatures)

    blockchain = [genesisBlock]  # List to store our blockchain
    timestamp = datetime.datetime.now()
    writeToLog("GENESIS BLOCK:0:[]:%s:[]"%(timestamp))

    if nodeName != 'client':
        serverThread = threading.Thread(target=serverThread)
        threads.append(serverThread)
        clientThread = threading.Thread(target=clientThread)
        threads.append(clientThread)
        serverThread.start()
        time.sleep(3)  # let the server thread have time to start on all nodes
        clientThread.start()
    else:
        while True:
            print()
            print("Enter integer selection (q to quit)")
            print("Create Transaction 1:")
            print("View Blockchain 2:")
            print("View Ledger 3: ")
            n = input("Please enter selection: ")

            if n is '1':
                print()
                transaction = createTransaction()
                print(transaction)
                clientSendToAll(transaction)
            elif n is '2':
                clientSendToAll("prntChain")
            elif n is '3':
                clientSendToAll("prntLdg")
            elif n is 'q':
                break
