from web3 import Web3
from decouple import config

INFURA_PROJECT_ID = config("INFURA_PROJECT_ID")
INFURA_PROJECT_SECRET = config("INFURA_PROJECT_SECRET")

# Fill in your infura API key here
infura_url = "https://:{secret}@mainnet.infura.io/v3/{proj_id}".format(proj_id = INFURA_PROJECT_ID, secret = INFURA_PROJECT_SECRET)
web3 = Web3(Web3.HTTPProvider(infura_url))

# get latest 10 blocks
latest = web3.eth.blockNumber
for i in range(0, 10):
  print(web3.eth.getBlock(latest - i))

