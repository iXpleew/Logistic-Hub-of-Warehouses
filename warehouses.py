class Warehouse:
    def __init__(self, name, max_capaci, curr_capaci=None, connections=None):
        self._name = name
        self._max_capaci = max_capaci
        if curr_capaci is not None:
            quantity_sum = 0
            for product in curr_capaci:
                quantity_sum += product["product_quantity"]
            if quantity_sum > max_capaci:
                raise ValueError("Current capacity larger than maximux")
        self._curr_capaci = curr_capaci
        self._connections = connections

    @property
    def name(self):
        return self._name

    @property
    def curr_capacity(self):
        return self._curr_capaci

    @property
    def connections(self):
        return self._connections

    def show_products(self):
        if self._curr_capaci is None:
            print("This Warehouse doesnt have anything inside")
        else:
            print("This Warehouse has: ")
            for prod in self._curr_capaci:
                print(f'{prod["product_name"]} - {prod["product_quantity"]}')

    def add_product(self):
        pass
