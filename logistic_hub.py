import warehouses
import networkx as nx
import matplotlib.pyplot as plt
import json


class LogisticHub:
    def __init__(self):
        with open("data.json", mode="r") as file:
            data = json.load(file)
        self._ware_graph = nx.Graph()
        for warehouse_data in data["warehouses"]:
            warehouse = warehouses.Warehouse(
                warehouse_data["name"],
                warehouse_data["max_capacity"],
                warehouse_data["current_capacity"])
            self._ware_graph.add_node(warehouse_data["name"], item=warehouse)

        for source in data["warehouses"]:
            for destination in source["connections"]:
                target = destination["target_name"]
                distance = destination["distance"]

                self._ware_graph.add_edge(
                    source["name"],
                    target,
                    weight=distance
                )

    def graph(self):
        return self._ware_graph


logisticHub = LogisticHub()
nx.draw(logisticHub.graph())
plt.show()
