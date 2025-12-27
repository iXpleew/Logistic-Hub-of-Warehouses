class Warehouse:
    def __init__(self, name, max_capacity):
        self._name = name
        self._max_capacity = max_capacity
        self._curr_capacity = 0
