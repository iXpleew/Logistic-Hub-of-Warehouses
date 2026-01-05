class Request:
    def __init__(self, product_name, capacity, source=None, destination=None):
        self._product_name = product_name
        self._capacity = capacity
        self._source = source
        self._destination = destination
    
    @property
    def capacity(self):
        return self._capacity
