class Warehouse:
    def __init__(self, name, max_capaci, curr_capaci=None, connections=None):
        self._name = name
        self._max_capaci = max_capaci
        self._curr_capaci = curr_capaci
        self._connections = connections
