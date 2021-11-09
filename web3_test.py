import time
import logging
import numpy as np
from web3 import Web3
from decouple import config
from datetime import datetime

INFURA_PROJECT_ID = config("INFURA_PROJECT_ID")
INFURA_PROJECT_SECRET = config("INFURA_PROJECT_SECRET")

start_time = time.time()
# Fill in your infura API key here
infura_url = "https://:{secret}@mainnet.infura.io/v3/{proj_id}".format(proj_id = INFURA_PROJECT_ID, secret = INFURA_PROJECT_SECRET)
web3 = Web3(Web3.HTTPProvider(infura_url))

# get latest 10 blocks
latest = web3.eth.blockNumber
#for i in range(0, 10):
#  print(web3.eth.getBlock(latest - i))
print("Block Number: {}".format(latest))
block_latest = web3.eth.get_block(latest-1)
transactions = block_latest["transactions"]
len_trans = len(transactions)
print("ETH Latest Block Number: {}".format(block_latest["number"]))
print("Number of transaction in block: {}".format(len_trans))
timestamp = block_latest["timestamp"]
print("Time: {}".format(datetime.fromtimestamp(timestamp)))
print("-------"*5)
wei = 0
for transaction in transactions:
    # Need to convert bytes to hexbytes using .hex() method
    info = web3.eth.get_transaction(transaction.hex())
    wei += info["value"]
eth = wei / 1000000000000000000
print("Total Value of Block: {}".format(eth))
logging.critical("Total execution time in seconds: %f" %(time.time()-start_time))


