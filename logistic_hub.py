import warehouses
import networkx as nx
# import matplotlib.pyplot as plt
import json


class LogisticHub:
    def __init__(self):
        with open("data.json", mode="r") as file:
            data = json.load(file)
        self.ware_graph = nx.Graph()
        for warehouse_data in data["warehouses"]:
            warehouse = warehouses.Warehouse(
                warehouse_data["name"],
                warehouse_data["max_capacity"],
                warehouse_data["current_capacity"])
            self.ware_graph.add_node(warehouse_data["name"], item=warehouse)

        for source in data["warehouses"]:
            for destination in source["connections"]:
                target = destination["target_name"]
                distance = destination["distance"]

                self.ware_graph.add_edge(
                    source,
                    target,
                    weight=distance
                )

# warehouse_graph.add_edge(first, second)
# nx.draw(warehouse_graph)
# plt.show()
