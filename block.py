from helpers import from_serialized, read_var_int

VERSION_BYTES = 4
PREVIOUS_HASH_BYTES = 32
MERKLE_ROOT_BYTES = 32
TIME_BYTES = 4
NBITS_BYTES = 4
NONCE_BYTES = 4


class Block(object):
    def __init__(self):
        self.version = None
        self.previous_hash = None
        self.merkle_root = None
        self.time = None
        self.nbits = None
        self.nonce = None
        self.transaction_count = None
        self.transactions = []

    def from_hex_dump(self, hex_file_path):
        with open(hex_file_path) as block_hex:
            self.version = from_serialized(block_hex.read(VERSION_BYTES * 2))
            self.previous_hash = from_serialized(block_hex.read(PREVIOUS_HASH_BYTES * 2))
            self.merkle_root = from_serialized(block_hex.read(MERKLE_ROOT_BYTES * 2))
            self.time = from_serialized(block_hex.read(TIME_BYTES * 2))
            self.nbits = from_serialized(block_hex.read(NBITS_BYTES * 2))
            self.nonce = from_serialized(block_hex.read(NONCE_BYTES * 2))
            self.transaction_count = read_var_int(block_hex)
            self._get_coinbase_transaction = self._get_coinbase_transaction(block_hex)

    def _get_coinbase_transaction(self, block_hex_file):
        self.transaction_version = from_serialized(block_hex_file.read(VERSION_BYTES * 2))
        print(self.transaction_version)
        tx_in = read_var_int(block_hex_file)
        coinbase_hash = from_serialized(block_hex_file.read(32*2))
        coinbase_index = from_serialized(block_hex_file.read(4*2))
        script_bytes = int(read_var_int(block_hex_file), 16)
        print(int(from_serialized(block_hex_file.read(8)), 16))


b = Block()
b.from_hex_dump('blocks/465086')

