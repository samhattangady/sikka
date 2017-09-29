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

    def execute(self):
        pass

