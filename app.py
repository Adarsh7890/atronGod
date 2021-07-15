from flask import Flask,request
import tronapi
from tronapi import Tron


full_node = 'https://api.trongrid.io'
solidity_node = 'https://api.trongrid.io'
event_server = 'https://api.trongrid.io'

PK = "ade6d2810038bbfa9eaa12241654546dc52336a10beb76ddd6c8156520580d6c"

tron = Tron(full_node=full_node,
    solidity_node=solidity_node,
    event_server=event_server)

def setTronPK(pk):
    tron.private_key = pk
    tron.default_address = tron.address.from_private_key(pk).base58

setTronPK(PK)

app = Flask(__name__)

def myfunc(add):
  txn = tron.trx.send_token(PA, 1*Ps, "1000645");
  return "ok"
 
app.route('/')
def getHandler():
    return "ok"

@app.route('/post', methods = ['POST'])
def getHandler():
     r = request.json
     PA = r["address"]
     PS = r["amount"]
     PR = r["tokenid"]
     txn = tron.trx.send_token(PA, 1*PS, PR);
     return txn["transaction"]["txID"]
    
    
   
if __name__ == '__main__':
 app.run()
