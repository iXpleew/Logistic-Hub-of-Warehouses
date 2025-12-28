class Warehouse:
    def __init__(self, name, max_capacity, curr_capacity, connections=None):
        self._name = name   
        self._max_capacity = max_capacity
        if curr_capacity > max_capacity:
            raise ValueError("Warehouse overloaded!")
        self._curr_capacity = curr_capacity
        self._connections = connections
