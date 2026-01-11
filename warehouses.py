class Warehouse:
    def __init__(self, name, max_capaci, curr_capacity=None, connections=None):
        self.name = name
        self.max_capacity = max_capaci
        if curr_capacity is not None and self.check_overload(curr_capacity):
            raise ValueError("Warehouse overloaded!")
        self.curr_capacity = curr_capacity
        self.connections = connections
        self.to_be_given = []

    def count_currentcapacity(self, products):
        if products is None:
            return 0
        quantity_sum = 0
        for product in products:
            quantity_sum += product["product_quantity"]
        return quantity_sum

    def is_there_a_product(self, name):
        if self.curr_capacity is None:
            return False
        for product in self.curr_capacity:
            if product["product_name"] == name:
                return True
        return False

    def check_overload(self, given_capacity, new_product=0):
        quantity_sum = new_product + self.count_currentcapacity(given_capacity)
        if quantity_sum > self.max_capacity:
            return True
        else:
            return False

    def requests_remaining(self):
        while self.to_be_given:
            request = self.to_be_given[0]
            if self.check_overload(self.curr_capacity, request.quantity):
                break
            else:
                self.adding_quantity(request)
                self.to_be_given.pop(0)

    def show_products(self):
        if self.curr_capacity is None:
            print("This Warehouse doesnt have anything inside")
        else:
            print("This Warehouse has: ")
            for prod in self.curr_capacity:
                print(f'{prod["product_name"]} - {prod["product_quantity"]}')
        print(f"Maximum quantity: {self.max_capacity}")

    def adding_quantity(self, request):
        demanded_product = request.product_name
        demanded_quantity = request.quantity

        if self.curr_capacity is None:
            self.curr_capacity = []
            self.curr_capacity.append({
                "product_name": demanded_product,
                "product_quantity": demanded_quantity
            })
            return
        else:
            for product in self.curr_capacity:
                if product["product_name"] == demanded_product:
                    product["product_quantity"] += demanded_quantity
                    return
            self.curr_capacity.append({
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
            self.to_be_given.append(request)
        else:
            self.adding_quantity(request)

    def remove_product(self, request):
        if self.curr_capacity is None:
            print("There is nothing in this warehouse")
            return False
        for product in self.curr_capacity:
            if product["product_name"] == request.product_name:
                left_products = product["product_quantity"] - request.quantity
                if left_products > 0:
                    product["product_quantity"] = left_products
                elif left_products == 0:
                    self.curr_capacity[:] = [x for x in self.curr_capacity if x["product_name"] != request.product_name]
                    print("Product has been removed succesfully!")
                else:
                    print("Not enough product in warehouse, proccess of removing denied")
                    return False
                return True
        print("Object wasn't found in this warehouse!")
        return False
