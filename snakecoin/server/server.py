# coding=utf-8
"""A node of the snakecoin blockchain"""
from datetime import datetime
import flask

from ..block import Block
from ..blockchain import Blockchain

blockchain = Blockchain()
miner_address = "Clinton"
node = flask.Flask(__name__)
transactions = []


def proof_of_work(last_proof):
    """Create a proof that work was completed while mining."""
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor


@node.route('/mine', methods=['GET'])
def mine():
    """Mine a snakecoin."""
    last_block = blockchain[-1]
    last_proof = last_block.data['proof-of-work']
    proof = proof_of_work(last_proof)
    transactions.append({"from": "network", "to": miner_address, "amount": 1})
    new_data = {"proof-of-work": proof, "transactions": transactions}
    new_index = last_block.index + 1
    mined_block = Block(new_index, datetime.now(), new_data, last_block.hash)
    blockchain.append(mined_block)
    return mined_block.json


@node.route('/transactions', methods=['POST'])
def transaction():
    """A new transaction occurance."""
    if flask.request.method == 'POST':
        new_transaction = flask.request.get_json()
        transactions.append(new_transaction)
        print("New transaction:")
        print(f"FROM: {new_transaction['from']}")
        print(f"TO: {new_transaction['to']}")
        print(f"AMOUNT: {new_transaction['amount']}")
        return True

node.run()
