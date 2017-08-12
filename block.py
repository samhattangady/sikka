from helpers import deserialize, read_var_int
from transaction import Transaction

VERSION_BYTES = 4
PREVIOUS_HASH_BYTES = 32
MERKLE_ROOT_BYTES = 32
TIME_BYTES = 4
NBITS_BYTES = 4
NONCE_BYTES = 4


class Block(object):
    """
    Blocks are the fundamental data structures in blockchain technology
    They contain details about transactions, the immediate previous
    block, the time when it was mined as well as the proof for the
    proof-of-work calculations that were conducted in its' mining.
    """

    @property
    def version(self):
        """
        The version of the block indicates which block validation rules
        are meant to be followed. This is useful while validating, and
        it allows for future developments and changes in block structure
        """
        return self._version

    @property
    def previous_hash(self):
        """
        The hash value of the previous block. This is used for blocks
        to be 'chained' to blocks that came before, effectively all
        the way back to the genesis block.
        """
        return self._previous_hash

    @property
    def merkle_root(self):
        """
        The merkle root is the root node of the merkle tree of all the
        transactions present in the block. It is an easily verifiable
        representation of all the transactions. This is required as the
        proof of work needs to include the proof of transactions.
        """
        return self._merkle_root

    @property
    def timestamp(self):
        """
        The UNIX timestamp of when the block was mined. It needs to be
        larger than the median of the previous 11 blocks' timestamps.
        This is to account for different miners, and nodes running 
        slightly differing clocks.
        """
        return self._timestamp

    @property
    def target(self):
        """
        The target is a threshhold that the header hash must be below
        for the block to be valid. This is the value that controls the
        difficulty that is adjusted every 2016 blocks.
        """
        return self._target

    @property
    def nonce(self):
        """
        The nonce is the value that is changed by the miner in order 
        to obtain the required hash. This is the value that proves the
        work done by the miner for this block.
        """
        return self._nonce

    @property
    def transaction_count(self):
        """
        The number of transactions present in the block.
        """
        return self._transaction_count

    @property
    def transactions(self):
        """
        List of all the transactions present in the block
        """
        return self._transactions

    def __init__(self):
        self._version = None
        self._previous_hash = None
        self._merkle_root = None
        self._timestamp = None
        self._target = None
        self._nonce = None
        self._transaction_count = None
        self._transactions = []

    def from_hex_dump(self, hex_file_path):
        with open(hex_file_path) as block_hex:
            self._version = deserialize(block_hex.read(VERSION_BYTES * 2))
            self._previous_hash = deserialize(block_hex.read(PREVIOUS_HASH_BYTES * 2))
            self._merkle_root = deserialize(block_hex.read(MERKLE_ROOT_BYTES * 2))
            self._timestamp = deserialize(block_hex.read(TIME_BYTES * 2))
            self._target = deserialize(block_hex.read(NBITS_BYTES * 2))
            self._nonce = deserialize(block_hex.read(NONCE_BYTES * 2))
            self._transaction_count = read_var_int(block_hex)
            self._get_coinbase_transaction = self._get_coinbase_transaction(block_hex)

    def _get_coinbase_transaction(self, block_hex_file):
        # TODO Push this to transaction.py
        transaction_version = deserialize(block_hex_file.read(VERSION_BYTES * 2))
        tx_in = read_var_int(block_hex_file)
        print(tx_in)
        coinbase_hash = deserialize(block_hex_file.read(32*2))
        coinbase_index = deserialize(block_hex_file.read(4*2))
        script_bytes = read_var_int(block_hex_file)
        print(script_bytes)
        coinbase_script = None
        height = int(deserialize(block_hex_file.read(2)),16)



b = Block()
b.from_hex_dump('blocks/465086')

