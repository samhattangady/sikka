from helpers import deserialize
from transaction import Transaction

VERSION_BYTES = 4
PREVIOUS_HASH_BYTES = 32
MERKLE_ROOT_BYTES = 32
TIME_BYTES = 4
NBITS_BYTES = 4
NONCE_BYTES = 4
INDEX_BYTES = 4
SEQUENCE_BYTES = 4
OUTPUT_VALUE_BYTES = 8


class Block(object):
    """
    Blocks are the fundamental data structures in blockchain technology
    They contain details about transactions, the immediate previous
    block, the time when it was mined as well as the proof for the
    proof-of-work calculations that were conducted in its' mining.
    """

    @property
    def bytes(self):
        """
        Raw byte version of the transaction
        """
        return self._bytes

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
        self._bytes = None
        self._version = None
        self._previous_hash = None
        self._merkle_root = None
        self._timestamp = None
        self._target = None
        self._nonce = None
        self._transaction_count = None
        self._transactions = []
        self._bytes_read = 0

    def parse_hex_dump(self, hex_file_path):
        with open(hex_file_path) as block_hex:
            self._bytes = block_hex.read()
        self._parse_header()
        self._parse_transactions()

    def _parse_header(self):
        self._version = deserialize(self._read_bytes(VERSION_BYTES))
        self._previous_hash = deserialize(self._read_bytes(PREVIOUS_HASH_BYTES))
        self._merkle_root = deserialize(self._read_bytes(MERKLE_ROOT_BYTES))
        self._timestamp = deserialize(self._read_bytes(TIME_BYTES))
        self._target = deserialize(self._read_bytes(NBITS_BYTES))
        self._nonce = deserialize(self._read_bytes(NONCE_BYTES))

    def _parse_transactions(self):
        self._transaction_count = self._read_var_int()
        for _ in range(self._transaction_count):
            self._transactions.append(self._parse_transaction())

    def _parse_transaction(self):
        version = self._read_bytes(VERSION_BYTES)
        number_of_inputs = self._read_var_int()
        inputs = []
        for _ in range(number_of_inputs):
            prev_tx_id = deserialize(self._read_bytes(PREVIOUS_HASH_BYTES))
            prev_tx_index = deserialize(self._read_bytes(INDEX_BYTES))
            script_bytes = self._read_var_int()
            signature_script = self._read_bytes(script_bytes)
            sequence = self._read_bytes(SEQUENCE_BYTES)
            inputs.append((prev_tx_id, prev_tx_index, signature_script, sequence))
        number_of_outputs = self._read_var_int()
        outputs = []
        for _ in range(number_of_outputs):
            value = deserialize(self._read_bytes(OUTPUT_VALUE_BYTES))
            script_bytes = self._read_var_int()
            output_script = self._read_bytes(script_bytes)
            outputs.append((value, output_script))
        lock_time = self._read_bytes(TIME_BYTES)
        return Transaction(version, inputs, outputs, lock_time)

    def _read_bytes(self, number_of_bytes):
        start_index = self._bytes_read * 2
        end_index = (self._bytes_read + number_of_bytes) * 2
        self._bytes_read += number_of_bytes
        return self._bytes[start_index:end_index]

    def _read_var_int(self):
        var_int = self._read_bytes(1)
        if var_int == 'fd':
            var_int = deserialize(self._read_bytes(2))
        elif var_int == 'fe':
            var_int = deserialize(self._read_bytes(3))
        elif var_int == 'ff':
            var_int = deserialize(self._read_bytes(4))
        return int(var_int, 16)


b = Block()
b.parse_hex_dump('blocks/465086')
