import warehouses
import networkx as nx
import matplotlib.pyplot as plt
import json


class LogisticHub:
    def __init__(self):
        self._ware_graph = nx.Graph()
        self._ware_list = []
        with open("data.json", mode="r") as file:
            data = json.load(file)
        for warehouse_data in data["warehouses"]:
            warehouse = warehouses.Warehouse(
                warehouse_data["name"],
                warehouse_data["max_capacity"],
                warehouse_data["current_capacity"])
            self._ware_graph.add_node(warehouse_data["name"], item=warehouse)
            self._ware_list.append(warehouse)

        for source in data["warehouses"]:
            for destination in source["connections"]:
                target = destination["target_name"]
                distance = destination["distance"]

                self._ware_graph.add_edge(
                    source["name"],
                    target,
                    weight=distance
                )

    @property
    def graph(self):
        return self._ware_graph


logisticHub = LogisticHub()
nx.draw(logisticHub.graph, with_labels=True)
plt.show()
