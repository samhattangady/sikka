import hashlib

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
        print('Script:', self._script)
        while self._execution_pointer < len(self._script) / 2:
            opcode = get_opcode(self._read_bytes(1))
            print(opcode)
            self._perform_operation(opcode)
            print(self._stack)

    def _perform_operation(self, opcode):
        if opcode in ['OP_FALSE']:
            self._stack.append(0)
        elif opcode in PUSH_CODES:
            num_bytes = PUSH_CODES.index(opcode)+1
            self._stack.append(self._read_bytes(num_bytes))
        elif opcode == 'OP_PUSHDATA1':
            num_bytes = int(self._read_bytes(1), 16)
            self._stack.append(self._read_bytes(num_bytes))
        elif opcode == 'OP_DUP':
            self._stack.append(self._stack[-1])
        elif opcode == 'OP_HASH160':
            operand = self._stack.pop()
            sha256 = hashlib.sha256(bytes(operand, 'ascii')).hexdigest()
            ripemd160 = hashlib.new('ripemd160')
            ripemd160.update(bytes(sha256, 'ascii'))
            self._stack.append(ripemd160.hexdigest())
        elif opcode == 'OP_EQUALVERIFY':
            lhs = self._stack.pop()
            rhs = self._stack.pop()
            result = lhs == rhs
            self._stack.append(result)
        else:
            exit()

