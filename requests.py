class Request:
    def __init__(self, product_name, quantity, source=None, destination=None):
        self.product_name = product_name
        self.quantity = quantity
        self.source = source
        self.destination = destination
