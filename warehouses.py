class Warehouse:
    def __init__(self, name, max_capaci, curr_capaci=None, connections=None):
        self._name = name
        self._max_capaci = max_capaci
        if curr_capaci is not None and self.check_overload(curr_capaci):
            raise ValueError("Warehouse overloaded!")
        self._curr_capaci = curr_capaci
        self._connections = connections
        self.requests_queue = []

    @property
    def name(self):
        return self._name

    @property
    def max_capacity(self):
        return self._max_capaci

    @property
    def curr_capacity(self):
        return self._curr_capaci

    @property
    def connections(self):
        return self._connections

    def check_overload(self, given_capacity, new_product=0):
        quantity_sum = new_product
        for product in given_capacity:
            quantity_sum += product["product_quantity"]
        if quantity_sum > self.max_capacity:
            return True
        else:
            return False

    def show_products(self):
        if self._curr_capaci is None:
            print("This Warehouse doesnt have anything inside")
        else:
            print("This Warehouse has: ")
            for prod in self._curr_capaci:
                print(f'{prod["product_name"]} - {prod["product_quantity"]}')

    def add_product(self, request):
        if self.check_overload(self.curr_capacity, request.capacity):
            pass
        pass
