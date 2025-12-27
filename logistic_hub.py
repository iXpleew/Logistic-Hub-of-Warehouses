import warehouses
import networkx as nx
import matplotlib.pyplot as plt


class LogisticHub:
    def __init__(self):
        self._warehouse_lists = []


warehouse_graph = nx.Graph()
first = warehouses.Warehouse("Warsaw", 2000)
second = warehouses.Warehouse("Cracow", 1500)

warehouse_graph.add_node(first)
warehouse_graph.add_node(second)

warehouse_graph.add_edge(first, second)
nx.draw(warehouse_graph)
plt.show()