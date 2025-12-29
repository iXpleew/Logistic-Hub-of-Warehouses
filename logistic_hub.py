from warehouses import Warehouse
import networkx as nx
import json
from matplotlib import pyplot as plt


class LogisticHub:
    def __init__(self, data_file):
        self._data_file = data_file
        self._ware_graph = nx.Graph()
        self.ware_list = []
        with open(data_file, mode="r") as file:
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

    def add_warehouse(self, name, max_capaci, curr_capaci, connect):
        new_warehouse = Warehouse(name, max_capaci, curr_capaci, connect)

        self.graph.add_node(name, item=new_warehouse)
        self.ware_list.append(new_warehouse)
        if new_warehouse.connections is not None:
            for connection in new_warehouse.connections:
                self.graph.add_edge(connection["target_name"],
                                    name,
                                    weight=connection["distance"])
        with open(self.data_file, mode="r") as file:
            data = json.load(file)
            warehouse_data = data["warehouses"]
            new_dict_warehouse = {
                "name": name,
                "max_capacity": max_capaci,
                "current_capacity": curr_capaci,
                "connections": connect
            }
            warehouse_data.append(new_dict_warehouse)

        with open(self.data_file, mode="w") as file:
            json.dump(data, file, indent=2)

    @property
    def data_file(self):
        return self._data_file

    @property
    def graph(self):
        return self._ware_graph

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
