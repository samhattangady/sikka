import hashlib

from helpers import deserialize
from opcodes import get_opcode, PUSH_CODES

class Script(object):

    @property
    def script(self):
        """
        The bytes that represent the script to be computed
        """
        return self._script

    def __init__(self, script):
        self._script = script
        self._stack = []
        self._alt_stack = []
        self._execution_pointer = 0

    def _read_bytes(self, number_of_bytes):
        start_index = self._execution_pointer * 2
        end_index = (self._execution_pointer + number_of_bytes) * 2
        self._execution_pointer += number_of_bytes
        return self._script[start_index:end_index]

    def execute(self):
        self._execution_pointer = 0
        self._stack = []
        self._alt_stack = []
        print('Script:', self._script)
        while self._execution_pointer < len(self._script) / 2:
            opcode = get_opcode(self._read_bytes(1))
            print(opcode)
            if not (self._perform_operation(opcode)):
                return False
            print(self._stack)
        result = self._stack.pop()
        if len(self._stack) == 0 or self._stack.pop() == 'OP_FALSE':
            return False
        return True

    def interpret(self):
        self._execution_pointer = 0
        while self._execution_pointer < len(self._script) / 2:
            opcode_byte = self._read_bytes(1)
            print(opcode_byte, end=' ')
            opcode = get_opcode(opcode_byte)
            print(opcode)
            if opcode in PUSH_CODES:
                num_bytes = PUSH_CODES.index(opcode)+1
                print(self._read_bytes(num_bytes))
            elif opcode == 'OP_PUSHDATA1':
                num_bytes = int(self._read_bytes(1), 16)
                print(self._read_bytes(num_bytes))

    def _perform_operation(self, opcode):
        if opcode in ['OP_FALSE']:
            self._stack.append(0)
            return True
        if opcode in PUSH_CODES:
            num_bytes = PUSH_CODES.index(opcode) + 1
            self._stack.append(self._read_bytes(num_bytes))
            return True
        if opcode == 'OP_PUSHDATA1':
            num_bytes = int(self._read_bytes(1), 16)
            self._stack.append(self._read_bytes(num_bytes))
            return True
        if opcode == 'OP_DUP':
            self._stack.append(self._stack[-1])
            return True
        if opcode == 'OP_HASH160':
            operand = self._stack.pop()
            sha256 = self._sha256(operand)
            hash160 = self._ripemd160(sha256)
            self._stack.append(hash160)
            return True
        if opcode == 'OP_EQUALVERIFY':
            return self._stack.pop() == self._stack.pop()

    def _sha256(self, hex_input):
        return hashlib.sha256(bytes.fromhex(hex_input)).hexdigest()

    def _ripemd160(self, hex_input):
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(bytes.fromhex(hex_input))
        return ripemd160.hexdigest()

