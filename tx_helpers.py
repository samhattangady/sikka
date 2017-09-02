class TxIn(object):
    def __init__(self, input_):
        self._prev_tx_id = input_[0]
        self._prev_tx_index = int(input_[1], 16)
        self._signature_script = input_[2]
        self._sequence = int(input_[3], 16)

class TxOut(object):
    def __init__(self, output):
        self._value = int(output[0], 16)
        self._output_script = output[1]

