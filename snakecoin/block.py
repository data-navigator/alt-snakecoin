# coding=utf-8
"""Creates the genesis block for the snakecoin blockchain."""
import datetime
import hashlib


class Block:
    """A block in the snakecoin blockchain."""
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __repr__(self):
        """Machine-readable self representation."""
        " ".join([str(self.index), str(self.timestamp), str(self.data),
                  str(self.previous_hash)])

    def hash_block(self):
        """Creates the sha256 hash for this Block."""
        sha = hashlib.sha256()
        sha.update(self.__repr__)
        return sha.hexdigest()

    def next_block(self):
        """Creates the next Block in the blockchain."""
        return Block(self.index + 1, self.timestamp, self.data, self.hash)


def create_genesis_block():
    """Manually construct a block with zero index and arbitrary previous hash
    value."""
    return Block(0, datetime.datetime.now(), 'genesis', '0')
