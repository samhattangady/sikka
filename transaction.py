from script import Script

class TxIn(object):
    def __init__(self, input_):
        self._prev_tx_id = input_[0]
        self._prev_tx_index = int(input_[1], 16)
        self._signature_script = Script(input_[2])
        self._sequence = int(input_[3], 16)


class TxOut(object):
    def __init__(self, output):
        self._value = int(output[0], 16)
        self._output_script = Script(output[1])


class Transaction(object):

    @property
    def version(self):
        """
        Version number of transaction
        As of 2017, all transactions are version 1
        Added to allow future evolution of transactions
        """
        return self._version

    @property
    def inputs(self):
        """
        List of TxIn
        Each TxIn contains the transaction id of the previous 
        transaction (the transaction that paid that address), the 
        index of the output from the same transaction, script that 
        unlocks the addresses as per the prev_tx, and sequence number
        (which allows txs to be updated)
        """
        return self._inputs

    @property
    def outputs(self):
        """
        List of TxOut
        Each TxOut contains the value being sent to the address, and a
        pk_script, which defines the requirements to spend from that 
        address
        """
        return self._outputs

    @property
    def lock_time(self):
        """
        The time until when the transaction is locked
        If the value is less than 500 million, it is a block height. 
        The transaction can only be added to a block with this height
        or higher. If the value is more than or equal to 500 million,
        it is a Unix epoch time. The transaction can only be added to
        a block whose timestamp is after this block.
        """
        return self._lock_time

    def __init__(self, version, inputs, outputs, lock_time):
        self._version = version
        self._inputs = [TxIn(input_) for input_ in inputs]
        self._outputs = [TxOut(output) for output in outputs]
        self._lock_time = int(lock_time, 16)