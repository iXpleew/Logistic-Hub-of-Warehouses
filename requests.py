class Request:
    def __init__(self, destination, capacity, source=None,):
        self._source = source
        self._destination = destination
        self._capacity = capacity
    
    @property
    def capacity(self):
        return self._capacity
