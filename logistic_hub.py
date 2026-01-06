from warehouses import Warehouse
from requests import Request
import networkx as nx
import json
from matplotlib import pyplot as plt


class LogisticHub:
    def __init__(self, data_file):
        self._data_file = data_file
        self._ware_graph = nx.Graph()
        self.ware_list = []
        self.load_hub()

    def add_edges_to_graph(self, warehouse: Warehouse):
        if warehouse.connections is None:
            return

        for connection in warehouse.connections:
            destination = connection["target_name"]
            distance = connection["distance"]

            self.graph.add_edge(
                warehouse.name,
                destination,
                weight=distance
            )
        pass

    def add_warehouse(self, name, max_capaci, curr_capaci, connect):
        new_warehouse = Warehouse(name, max_capaci, curr_capaci, connect)

        self.graph.add_node(name, item=new_warehouse)
        self.ware_list.append(new_warehouse)
        self.add_edges_to_graph(new_warehouse)

    def start_request(self, source, destination, name, quantity):
        request = Request(name, quantity, source, destination)
        source_warehouse = self.return_warehouse(source)
        destination_warehouse = self.return_warehouse(destination)

        if source_warehouse is None or destination_warehouse is None:
            return print("One of these warehouses doesnt exist, request cancelled!")

        if destination_warehouse.max_capacity > request.quantity:
            pass
        pass

    def search_product(self, name):
        for house in self.ware_list:
            for product in house.curr_capacity:
                if product["product_name"] == name:
                    print(f"{house.name} has {name}!")

    def add_product(self, warehouse_name, name, quantity):
        warehouse = self.return_warehouse(warehouse_name)
        if warehouse is None:
            return print("Cannot add product to no-existing warehouse")
        request = Request(product_name=name, quantity=quantity)
        warehouse.add_product(request)
        pass

    def remove_product(self, warehouse_name, name, quantity):
        warehouse = self.return_warehouse(warehouse_name)
        if warehouse is None:
            return print("Cannot remove product form no-existing warehouse")
        request = Request(product_name=name, quantity=quantity)
        warehouse.remove_product(request)
        pass

    def show_actual_requests(self):
        pass

    def return_warehouse(self, warehouse_name):
        for warehouse in self.ware_list:
            if warehouse.name == warehouse_name:
                return warehouse
        return None

    def show_what_warehouse_has(self, warehouse_name):
        warehouse = self.return_warehouse(warehouse_name)
        if warehouse is None:
            return print("That warehouse doesnt exist")
        else:
            warehouse.show_products()

    def save_hub(self):
        warehouse_list = []
        for warehouse in self.ware_list:
            new_dict = {
                "name": warehouse.name,
                "max_capacity": warehouse.max_capacity,
                "current_capacity": warehouse.curr_capacity,
                "connections": warehouse.connections
            }
            warehouse_list.append(new_dict)
        with open("testing_data.json", mode="w") as file:
            json.dump({"warehouses": warehouse_list}, file, indent=2)

    def load_hub(self):
        self.ware_list.clear()
        with open(self.data_file, mode="r") as file:
            data = json.load(file)
        for warehouse_data in data["warehouses"]:
            warehouse = Warehouse(
                warehouse_data["name"],
                warehouse_data["max_capacity"],
                warehouse_data["current_capacity"],
                warehouse_data["connections"])
            self._ware_graph.add_node(warehouse_data["name"], item=warehouse)
            self.ware_list.append(warehouse)

        for warehouse in self.ware_list:
            self.add_edges_to_graph(warehouse)

    @property
    def data_file(self):
        return self._data_file

    @property
    def graph(self):
        return self._ware_graph

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
