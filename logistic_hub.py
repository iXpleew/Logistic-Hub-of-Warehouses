from warehouses import Warehouse
import networkx as nx
import json
from matplotlib import pyplot as plt


class LogisticHub:
    def __init__(self, file):
        self._ware_graph = nx.Graph()
        self.ware_list = []
        with open(file, mode="r") as file:
            data = json.load(file)
        for warehouse_data in data["warehouses"]:
            warehouse = Warehouse(
                warehouse_data["name"],
                warehouse_data["max_capacity"],
                warehouse_data["current_capacity"])
            self._ware_graph.add_node(warehouse_data["name"], item=warehouse)
            self.ware_list.append(warehouse)

        for source in data["warehouses"]:
            for destination in source["connections"]:
                target = destination["target_name"]
                distance = destination["distance"]

                self.graph.add_edge(
                    source["name"],
                    target,
                    weight=distance
                )

    def add_warehuse(self, name, max_capaci, curr_capaci, connections):
        new_warehouse = Warehouse(name, max_capaci, curr_capaci, connections)
        self.graph.add_node(name, item=new_warehouse)
        self.ware_list.append(new_warehouse)
        if new_warehouse.connections is not None:
            for connection in new_warehouse.connections:
                self.graph.add_edge(connection["target_name"],
                                    name,
                                    weight=connection["distance"])

    @property
    def graph(self):
        return self._ware_graph

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
