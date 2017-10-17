# coding=utf-8
"""Creates the genesis block for the snakecoin blockchain."""
import hashlib
import json


class Block:
    """A block in the snakecoin blockchain."""
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """Creates the sha256 hash for this Block."""
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') + 
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    @property
    def json(self):
        """Return a JSON representation of this Block."""
        return json.dumps({"index": self.index,
                           "timestamp": str(self.timestamp),
                           "data": self.data,
                           "hash": self.hash})

    def next_block(self):
        """Creates the next Block in the blockchain."""
        return Block(self.index + 1, self.timestamp, self.data, self.hash)
