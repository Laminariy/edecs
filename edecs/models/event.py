class Event():
    '''Event class'''

    @property
    def type(self):
        return self._type

    @property
    def data(self):
        return self._data


    def __init__(self, type, data):
        self._type = type
        self._data = data
