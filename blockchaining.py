#Blockchaining program
import os.path
import csv 
import datetime
import hashlib

#initialising nonce and hash for previous block
index = 0
previous_block_hash = None

#setting dummy first block
def first_block():
    global index
    global previous_block_hash
    data = 'first block'
    timestamp = datetime.datetime.now()
    sha = hashlib.sha256(data.encode()).hexdigest()
    bchaining.write('Index: ' + str(index) + '\n ' + 'data: ' + data + '\n ' + 'Timestamp: ' + str(timestamp) + '\n' + str(sha) + '\n' + '\n')
    previous_block_hash = sha

#reading the transaction from csv file
def readtransaction():
    global index
    data = [] #empty array initialise
    #check whether the file is empty or not
    if os.path.getsize('Transaction_Recording.csv') == 0:
        return 0
    with open ('Transaction_Recording.csv' , newline = '' ) as trecording:
        treader = csv.reader(trecording)
        for row in treader:
            data.append(row) #adding rows from trecording to data array
    trecording.close()
    index = len(data)
    return data[-1] 

#writing transaction to blockchaining file
def calculateNonce(tdata):
    global index
    global previous_block_hash
    encodestr = '' #new empty block of transaction
    for value in tdata:
            encodestr += value  #value from tdata concatenate to encodestr
    encodestr += str(index) + str(previous_block_hash) 
    nonce = 0
    #loop to calculate nonce and hash
    while 1:
        encodestr += str(nonce)
        encodestr_hash = hashlib.sha256(encodestr.encode()).hexdigest()
        #check if hash has 14 zeros
        zerocount = "0"
        numberofzero = str(encodestr_hash).count(zerocount)
        if numberofzero == 14:
            bchaining.write('Index: ' + str(index) + '\n' +
                            'data: ' + tdata[0] + ' ' + tdata[1]+ ' '+ tdata[2] + ' ' + tdata[3] + '\n' +
                            'proof of work: ' + str(nonce) + '\n' +
                            'hash: ' + str(encodestr_hash) + '\n')
            previous_block_hash = str(encodestr_hash)
            break
        
        #check if the value of nonce exceeds 50000
        if nonce >= 50000:
            bchaining.write('Index: ' + str(index) + '\n' +
                            'data: ' + tdata[0] + ' ' + tdata[1]+ ' '+ tdata[2] + ' ' + tdata[3] + '\n' +
                            'proof of work: ' + str(nonce) + '\n' +
                            'hash: ' + str(encodestr_hash) + '\n' )
            previous_block_hash = str(encodestr_hash)
            break
            
        nonce += 1

#opening block chaining file to write      
while 1:
    bchaining = open ('blockchaining.txt' , 'a')
    old_index = index

    if os.path.getsize('blockchaining.txt') == 0:
        first_block()
    tdata = readtransaction()#returns the data from read transaction to tdata
    
    if tdata != 0 and old_index != index:
        calculateNonce(tdata) #passing value of tdata to myfunction
    bchaining.close()
