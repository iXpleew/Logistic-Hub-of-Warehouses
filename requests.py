class Request:
    def __init__(self, product_name, quantity, source=None, destination=None):
        self._product_name = product_name
        self._quantity = quantity
        self._source = source
        self._destination = destination

    @property
    def product_name(self):
        return self._product_name

    @property
    def quantity(self):
        return self._quantity

    @property
    def source(self):
        return self._source

    @property
    def destination(self):
        return self._destination
