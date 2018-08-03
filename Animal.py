class Animal(object):

    def __init__(self, name):
        self._name = name

    def run(self):
        print(self._name, "running")

    @property
    def name(self):
        return self._name
