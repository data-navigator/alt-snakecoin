# coding=utf-8
"""The snakecoin Blockchain server."""
import datetime

from .block import Block


class Blockchain:
    """A snakecoin blockchain."""
    def __init__(self):
        self.blockchain = [Blockchain._create_genesis_block()]

    @staticmethod
    def _create_genesis_block():
        """Manually construct a block with zero index and arbitrary previous
        hash value."""
        return Block(0, datetime.datetime.now(), 'genesis', '0')

    def latest(self):
        """Return the most recently added Block to the Blockchain."""
        return self.blockchain[-1]

    def add(self, blocks_to_add):
        """Add a given number of blocks to the blockchain."""
        for _ in range(blocks_to_add):
            block = self.latest()
            self.blockchain.append(block.next_block())
            print(f"Block {block.index} has been added to the blockchain!")
            print(f"Hash: {block.hash}\n")
