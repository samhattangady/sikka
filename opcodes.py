_OPCODES = {
    0: 'OP_FALSE',
    1: 'OP_PUSH1',
    2: 'OP_PUSH2',
    3: 'OP_PUSH3',
    4: 'OP_PUSH4',
    5: 'OP_PUSH5',
    6: 'OP_PUSH6',
    7: 'OP_PUSH7',
    8: 'OP_PUSH8',
    9: 'OP_PUSH9',
    10: 'OP_PUSH10',
    11: 'OP_PUSH11',
    12: 'OP_PUSH12',
    13: 'OP_PUSH13',
    14: 'OP_PUSH14',
    15: 'OP_PUSH15',
    16: 'OP_PUSH16',
    17: 'OP_PUSH17',
    18: 'OP_PUSH18',
    19: 'OP_PUSH19',
    20: 'OP_PUSH20',
    21: 'OP_PUSH21',
    22: 'OP_PUSH22',
    23: 'OP_PUSH23',
    24: 'OP_PUSH24',
    25: 'OP_PUSH25',
    26: 'OP_PUSH26',
    27: 'OP_PUSH27',
    28: 'OP_PUSH28',
    29: 'OP_PUSH29',
    30: 'OP_PUSH30',
    31: 'OP_PUSH31',
    32: 'OP_PUSH32',
    33: 'OP_PUSH33',
    34: 'OP_PUSH34',
    35: 'OP_PUSH35',
    36: 'OP_PUSH36',
    37: 'OP_PUSH37',
    38: 'OP_PUSH38',
    39: 'OP_PUSH39',
    40: 'OP_PUSH40',
    41: 'OP_PUSH41',
    42: 'OP_PUSH42',
    43: 'OP_PUSH43',
    44: 'OP_PUSH44',
    45: 'OP_PUSH45',
    46: 'OP_PUSH46',
    47: 'OP_PUSH47',
    48: 'OP_PUSH48',
    49: 'OP_PUSH49',
    50: 'OP_PUSH50',
    51: 'OP_PUSH51',
    52: 'OP_PUSH52',
    53: 'OP_PUSH53',
    54: 'OP_PUSH54',
    55: 'OP_PUSH55',
    56: 'OP_PUSH56',
    57: 'OP_PUSH57',
    58: 'OP_PUSH58',
    59: 'OP_PUSH59',
    60: 'OP_PUSH60',
    61: 'OP_PUSH61',
    62: 'OP_PUSH62',
    63: 'OP_PUSH63',
    64: 'OP_PUSH64',
    65: 'OP_PUSH65',
    66: 'OP_PUSH66',
    67: 'OP_PUSH67',
    68: 'OP_PUSH68',
    69: 'OP_PUSH69',
    70: 'OP_PUSH70',
    71: 'OP_PUSH71',
    72: 'OP_PUSH72',
    73: 'OP_PUSH73',
    74: 'OP_PUSH74',
    75: 'OP_PUSH75',
    76: 'OP_PUSHDATA1',
    77: 'OP_PUSHDATA2',
    78: 'OP_PUSHDATA4',
    79: 'OP_1NEGATE',
    80: 'OP_RESERVED',
    81: 'OP_TRUE',
    82: 'OP_2',
    83: 'OP_3',
    84: 'OP_4',
    85: 'OP_5',
    86: 'OP_6',
    87: 'OP_7',
    88: 'OP_8',
    89: 'OP_9',
    90: 'OP_10',
    91: 'OP_11',
    92: 'OP_12',
    93: 'OP_13',
    94: 'OP_14',
    95: 'OP_15',
    96: 'OP_16',
    97: 'OP_NOP',
    98: 'OP_VER',
    99: 'OP_IF',
    100: 'OP_NOTIF',
    101: 'OP_VERIF',
    102: 'OP_VERNOTIF',
    103: 'OP_ELSE',
    104: 'OP_ENDIF',
    105: 'OP_VERIFY',
    106: 'OP_RETURN',
    107: 'OP_TOALTSTACK',
    108: 'OP_FROMALTSTACK',
    109: 'OP_2DROP',
    110: 'OP_2DUP',
    111: 'OP_3DUP',
    112: 'OP_2OVER',
    113: 'OP_2ROT',
    114: 'OP_2SWAP',
    115: 'OP_IFDUP',
    116: 'OP_DEPTH',
    117: 'OP_DROP',
    118: 'OP_DUP',
    119: 'OP_NIP',
    120: 'OP_OVER',
    121: 'OP_PICK',
    122: 'OP_ROLL',
    123: 'OP_ROT',
    124: 'OP_SWAP',
    125: 'OP_TUCK',
    126: 'OP_CAT',
    127: 'OP_SUBSTR',
    128: 'OP_LEFT',
    129: 'OP_RIGHT',
    130: 'OP_SIZE',
    131: 'OP_INVERT',
    132: 'OP_AND',
    133: 'OP_OR',
    134: 'OP_XOR',
    135: 'OP_EQUAL',
    136: 'OP_EQUALVERIFY',
    137: 'OP_RESERVED1',
    138: 'OP_RESERVED2',
    139: 'OP_1ADD',
    140: 'OP_1SUB',
    141: 'OP_2MUL',
    142: 'OP_2DIV',
    143: 'OP_NEGATE',
    144: 'OP_ABS',
    145: 'OP_NOT',
    146: 'OP_0NOTEQUAL',
    147: 'OP_ADD',
    148: 'OP_SUB',
    149: 'OP_MUL',
    150: 'OP_DIV',
    151: 'OP_MOD',
    152: 'OP_LSHIFT',
    153: 'OP_RSHIFT',
    154: 'OP_BOOLAND',
    155: 'OP_BOOLOR',
    156: 'OP_NUMEQUAL',
    157: 'OP_NUMEQUALVERIFY',
    158: 'OP_NUMNOTEQUAL',
    159: 'OP_LESSTHAN',
    160: 'OP_GREATERTHAN',
    161: 'OP_LESSTHANOREQUAL',
    162: 'OP_GREATERTHANOREQUAL',
    163: 'OP_MIN',
    164: 'OP_MAX',
    165: 'OP_WITHIN',
    166: 'OP_RIPEMD160',
    167: 'OP_SHA1',
    168: 'OP_SHA256',
    169: 'OP_HASH160',
    170: 'OP_HASH256',
    171: 'OP_CODESEPARATOR',
    172: 'OP_CHECKSIG',
    173: 'OP_CHECKSIGVERIFY',
    174: 'OP_CHECKMULTISIG',
    175: 'OP_CHECKMULTISIGVERIFY',
    176: 'OP_NOP1',
    177: 'OP_CHECKLOCKTIMEVERIFY',
    178: 'OP_CHECKSEQUENCEVERIFY',
    179: 'OP_NOP4',
    180: 'OP_NOP5',
    181: 'OP_NOP6',
    182: 'OP_NOP7',
    183: 'OP_NOP8',
    184: 'OP_NOP9',
    185: 'OP_NOP10',
    186: 'UNASSIGNED',
    187: 'UNASSIGNED',
    188: 'UNASSIGNED',
    189: 'UNASSIGNED',
    190: 'UNASSIGNED',
    191: 'UNASSIGNED',
    192: 'UNASSIGNED',
    193: 'UNASSIGNED',
    194: 'UNASSIGNED',
    195: 'UNASSIGNED',
    196: 'UNASSIGNED',
    197: 'UNASSIGNED',
    198: 'UNASSIGNED',
    199: 'UNASSIGNED',
    200: 'UNASSIGNED',
    201: 'UNASSIGNED',
    202: 'UNASSIGNED',
    203: 'UNASSIGNED',
    204: 'UNASSIGNED',
    205: 'UNASSIGNED',
    206: 'UNASSIGNED',
    207: 'UNASSIGNED',
    208: 'UNASSIGNED',
    209: 'UNASSIGNED',
    210: 'UNASSIGNED',
    211: 'UNASSIGNED',
    212: 'UNASSIGNED',
    213: 'UNASSIGNED',
    214: 'UNASSIGNED',
    215: 'UNASSIGNED',
    216: 'UNASSIGNED',
    217: 'UNASSIGNED',
    218: 'UNASSIGNED',
    219: 'UNASSIGNED',
    220: 'UNASSIGNED',
    221: 'UNASSIGNED',
    222: 'UNASSIGNED',
    223: 'UNASSIGNED',
    224: 'UNASSIGNED',
    225: 'UNASSIGNED',
    226: 'UNASSIGNED',
    227: 'UNASSIGNED',
    228: 'UNASSIGNED',
    229: 'UNASSIGNED',
    230: 'UNASSIGNED',
    231: 'UNASSIGNED',
    232: 'UNASSIGNED',
    233: 'UNASSIGNED',
    234: 'UNASSIGNED',
    235: 'UNASSIGNED',
    236: 'UNASSIGNED',
    237: 'UNASSIGNED',
    238: 'UNASSIGNED',
    239: 'UNASSIGNED',
    240: 'UNASSIGNED',
    241: 'UNASSIGNED',
    242: 'UNASSIGNED',
    243: 'UNASSIGNED',
    244: 'UNASSIGNED',
    245: 'UNASSIGNED',
    246: 'UNASSIGNED',
    247: 'UNASSIGNED',
    248: 'UNASSIGNED',
    249: 'UNASSIGNED',
    250: 'UNASSIGNED',
    251: 'UNASSIGNED',
    252: 'UNASSIGNED',
    253: 'OP_PUBKEYHASH',
    254: 'OP_PUBKEY',
    255: 'OP_INVALIDOPCODE'
}

INVALID_OPCODES = ['UNASSIGNED', 'OPVERIF', 'OP_VERNOTIF', 'OP_MUL', 'OP_MOD',
    'OP_DIV', 'OP_2MUL', 'OP_2DIV', 'OP_INVERT', 'OP_AND', 'OP_OR', 'OP_XOR',
    'OP_CAT', 'OP_SUBSTR', 'OP_LEFT', 'OP_RIGHT', 'OP_PUBKEYHASH', 'OP_PUBKEY',
    'OP_INVALIDOPCODE']

PUSH_CODES = ['OP_PUSH1', 'OP_PUSH2', 'OP_PUSH3', 'OP_PUSH4', 'OP_PUSH5',
              'OP_PUSH6', 'OP_PUSH7', 'OP_PUSH8', 'OP_PUSH9', 'OP_PUSH10',
              'OP_PUSH11', 'OP_PUSH12', 'OP_PUSH13', 'OP_PUSH14','OP_PUSH15',
              'OP_PUSH16', 'OP_PUSH17', 'OP_PUSH18', 'OP_PUSH19', 'OP_PUSH20',
              'OP_PUSH21', 'OP_PUSH22', 'OP_PUSH23', 'OP_PUSH24', 'OP_PUSH25',
              'OP_PUSH26', 'OP_PUSH27', 'OP_PUSH28', 'OP_PUSH29', 'OP_PUSH30',
              'OP_PUSH31', 'OP_PUSH32', 'OP_PUSH33', 'OP_PUSH34', 'OP_PUSH35',
              'OP_PUSH36', 'OP_PUSH37', 'OP_PUSH38', 'OP_PUSH39', 'OP_PUSH40',
              'OP_PUSH41', 'OP_PUSH42', 'OP_PUSH43', 'OP_PUSH44', 'OP_PUSH45',
              'OP_PUSH46', 'OP_PUSH47', 'OP_PUSH48', 'OP_PUSH49', 'OP_PUSH50',
              'OP_PUSH51', 'OP_PUSH52', 'OP_PUSH53', 'OP_PUSH54', 'OP_PUSH55',
              'OP_PUSH56', 'OP_PUSH57', 'OP_PUSH58', 'OP_PUSH59', 'OP_PUSH60',
              'OP_PUSH61', 'OP_PUSH62', 'OP_PUSH63', 'OP_PUSH64', 'OP_PUSH65',
              'OP_PUSH66', 'OP_PUSH67', 'OP_PUSH68', 'OP_PUSH69', 'OP_PUSH70',
              'OP_PUSH71', 'OP_PUSH72', 'OP_PUSH73', 'OP_PUSH74', 'OP_PUSH75']

def get_opcode(hex):
    try:
        return _OPCODES[int(hex, 16)]
    except KeyError:
        raise (ValueError, 'op code must be hex between 00 and ff')

