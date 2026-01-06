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

    def count_currentcapacity(self, products):
        if products is None:
            return 0
        quantity_sum = 0
        for product in products:
            quantity_sum += product["product_quantity"]
        return quantity_sum

    def check_overload(self, given_capacity, new_product=0):
        quantity_sum = new_product + self.count_currentcapacity(given_capacity)
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

    def editing_quantity(self, request):
        demanded_product = request.product_name
        demanded_quantity = request.quantity

        if self.curr_capacity is None:
            self._curr_capacity = []
            self._curr_capacity.append({
                "product_name": demanded_product,
                "product_quantity": demanded_quantity
            })
            return
        for product in self.curr_capacity:
            if product["product_name"] == demanded_product:
                product["product_quantity"] += demanded_quantity
                return
        self._curr_capacity.append({
            "product_name": demanded_product,
            "product_quantity": demanded_quantity
        })

    def add_product(self, request):
        if self.check_overload(self.curr_capacity, request.quantity):
            if request.quantity > self.max_capacity:
                print("Request cancelled, because its quantity is bigger than maximum capacity!")
                return False
            print(f"That request makes {self.name} overloaded!")
            print("Request is queued!")
            self.requests_queue.append(request)
        else:
            self.editing_quantity(request)

    def remove_product(self, request):
        if self.curr_capacity is None:
            print("There is nothing in this warehouse")
            return False
        for product in self.curr_capacity:
            if product["product_name"] == request.product_name:
                left_products = product["product_quantity"] - request.quantity
                if left_products > 0:
                    product["product_quantity"] = left_products
                    return True
                else:
                    self.curr_capacity[:] = [x for x in self.curr_capacity if x["product_name"] != request.product_name]
                    print(f"For simplification, that request deleted all of the {request.product_name}!")
                    return True
        print("Object wasn't found in this warehouse!")
        return False
