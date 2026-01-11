from warehouses import Warehouse
from requests import Request
import networkx as nx
import json
from matplotlib import pyplot as plt


class LogisticHub:
    def __init__(self, data_file):
        self.data_file = data_file
        self.graph = nx.Graph()
        self.ware_list = []
        self.requests_list = []

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

    def start_request(self, source: str, destination: str, name: str, quantity: int):
        if source == destination:
            return print("Request to the same warehouse is forbidden")
        request = Request(name, quantity, source, destination)
        source_warehouse = self.return_warehouse(source)
        destination_warehouse = self.return_warehouse(destination)
        if source_warehouse is None or destination_warehouse is None:
            return print("One of these warehouses doesnt exist, request cancelled!")

        if not nx.has_path(self.graph, source, destination):
            raise nx.NetworkXNoPath("Path between warehouses does no exist - request denied")

        if destination_warehouse.max_capacity < request.quantity:
            return print("Request's capacity is bigger than maximum capacity")

        if not source_warehouse.is_there_a_product(name):
            return print(f"This product is not in {source}")

        print("Request is accepted!")
        self.requests_list.append(request)

    def skip_time(self):
        # checking if there are products that can be sent right now
        for warehouse in self.ware_list:
            warehouse.requests_remaining()

        # and now doing requests
        for request in self.requests_list[:]:
            source = self.return_warehouse(request.source)
            destination = self.return_warehouse(request.destination)
            if source is not None and destination is not None and source.remove_product(request):
                destination.add_product(request)
            else:
                print("This request cannot be handled so it's denied")
            self.requests_list.remove(request)

    def clear_requests(self):
        self.requests_list.clear()

    def search_product(self, name: str):
        for house in self.ware_list:
            for product in house.curr_capacity:
                if product["product_name"] == name:
                    print(f"{house.name} has {name}!")

    def add_product(self, warehouse_name: str, name: str, quantity: int):
        warehouse = self.return_warehouse(warehouse_name)
        if warehouse is None:
            return print("Cannot add product to no-existing warehouse")
        request = Request(product_name=name, quantity=quantity, destination=warehouse_name)
        warehouse.add_product(request)
        pass

    def remove_product(self, warehouse_name: str, name: str, quantity: int):
        warehouse = self.return_warehouse(warehouse_name)
        if warehouse is None:
            return print("Cannot remove product form no-existing warehouse")
        request = Request(product_name=name, quantity=quantity, source=warehouse)

        if warehouse.remove_product(request):
            return True
        else:
            return False

    def show_actual_requests(self):
        print("******* DELIVERIES *******")
        for request in self.requests_list:
            print(f"FROM: {request.source}")
            print(f"TO: {request.destination}")
            print(f"{request.product_name} - {request.quantity}")
            bypassed_cities = nx.dijkstra_path(self.graph, request.source, request.destination)
            distance = nx.dijkstra_path_length(self.graph, request.source, request.destination)
            print(f"Through: {bypassed_cities} and total distance is {distance}")
            print()

    def return_warehouse(self, warehouse_name: str):
        for warehouse in self.ware_list:
            if warehouse.name == warehouse_name:
                return warehouse
        return None

    def show_what_warehouse_has(self, warehouse_name: str):
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
        with open(self.data_file, mode="w") as file:
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
            self.graph.add_node(warehouse_data["name"], item=warehouse)
            self.ware_list.append(warehouse)

        for warehouse in self.ware_list:
            self.add_edges_to_graph(warehouse)

    def draw_graph(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()
