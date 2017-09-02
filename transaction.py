class Transaction(object):
    def __init__(self, version, inputs, outputs, lock_time):
        self._version = version
        self._inputs = inputs
        self._outputs = outputs
        self._lock_time = lock_time