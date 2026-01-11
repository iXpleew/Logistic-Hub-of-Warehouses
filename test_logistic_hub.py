from logistic_hub import LogisticHub
import networkx as nx
import pytest

invalid_data = "invalid_data.json"
valid_data = "data.json"
test_data = "testing_data.json"


def test_creating_logistic_hub():
    _ = LogisticHub(valid_data)


def test_maximum_capacity_overreached():
    with pytest.raises(ValueError):
        _ = LogisticHub(invalid_data)


def test_return_correct_data_file():
    hub = LogisticHub(valid_data)
    assert valid_data == hub.data_file


def test_graph_edge_existance():
    hub = LogisticHub(test_data)
    assert hub.graph.has_edge("Warsaw Hub", "Lodz Depot") is True


def test_graph_edge_no_existance():
    hub = LogisticHub(test_data)
    assert hub.graph.has_edge("Poznan Annex", "Cracow Center") is False


def test_graph_weight():
    hub = LogisticHub(test_data)
    distance = hub.graph.edges["Warsaw Hub", "Gdansk Port"]["weight"]
    assert distance == 340


def test_correct_number_of_warehouses_as_nodes():
    hub = LogisticHub(test_data)
    assert hub.graph.number_of_nodes() == 6


def test_correct_number_of_edges():
    hub = LogisticHub(test_data)
    assert hub.graph.number_of_edges() == 6


def test_warehouse_with_no_edges():
    hub = LogisticHub(test_data)
    with pytest.raises(nx.NetworkXNoPath):
        hub.start_request("Cracow Center", "Moscow Mall", "Apple", 10)


def test_number_of_all_connection_of_a_warehouse():
    hub = LogisticHub(test_data)
    warehouse = hub.return_warehouse("Lodz Depot")
    lodz_connections = 3
    counter = 0
    if warehouse is not None:
        for con in warehouse.connections:
            counter += 1
    assert lodz_connections == counter


def test_looking_for_warehouse():
    hub = LogisticHub(test_data)
    current_warehouse = None
    for warehouse in hub.ware_list:
        if warehouse.name == "Warsaw Hub":
            current_warehouse = warehouse
            break
    assert current_warehouse is not None


def test_looking_for_warehouse_that_doesnt_exist():
    hub = LogisticHub(test_data)
    current_warehouse = None
    for warehouse in hub.ware_list:
        if warehouse.name == "Wroclaw Warehouse":
            current_warehouse = warehouse
            break
    assert current_warehouse is None


def test_adding_item_to_warehouse_that_doesnt_have_it():
    hub = LogisticHub(test_data)
    hub.add_product("Warsaw Hub", "Potato", 10)
    warehouse = hub.return_warehouse("Warsaw Hub")
    found = False
    if warehouse is not None:
        for product in warehouse.curr_capacity:
            if product["product_name"] == "Potato":
                found = True
    assert found is True


def test_removing_unexisting_item_from_warehouse():
    hub = LogisticHub(test_data)
    assert hub.remove_product("Warsaw Hub", "Potato", 10) is False


def test_removing_existing_item():
    hub = LogisticHub(test_data)
    assert hub.remove_product("Warsaw Hub", "Carrot", 200) is True


def test_removing_too_much_existing_item():
    hub = LogisticHub(test_data)
    assert hub.remove_product("Warsaw Hub", "Carrot", 20000) is False


def test_requesting():
    hub = LogisticHub(test_data)
    first_lenght = len(hub.requests_list)
    hub.start_request("Warsaw Hub", "Gdansk Port", "Carrot", 200)
    second_lenght = len(hub.requests_list)
    assert first_lenght == 0 and second_lenght == 1


def test_not_requesting():
    hub = LogisticHub(test_data)
    first_lenght = len(hub.requests_list)
    hub.start_request("Warsaw Hub", "Gdansk Port", "Carrot", 2000000)
    second_lenght = len(hub.requests_list)
    assert first_lenght == 0 == second_lenght


def test_deleting_from_source_adding_to_destination():
    hub = LogisticHub(test_data)
    hub.start_request("Poznan Annex", "Cracow Center", "Cucumber", 200)
    hub.skip_time()

    cucumbers_in_poznan = False
    cucumbers_in_cracow = False

    poznan = hub.return_warehouse("Poznan Annex")
    cracow = hub.return_warehouse("Cracow Center")

    if poznan and cracow is not None:
        for product in poznan.curr_capacity:
            if product["product_name"] == "Cucumber":
                cucumbers_in_poznan = True
        for product in cracow.curr_capacity:
            if product["product_name"] == "Cucumber" and product["product_quantity"] == 200:
                cucumbers_in_cracow = True
    assert cucumbers_in_poznan is False and cucumbers_in_cracow is True


def test_queueing_request():
    hub = LogisticHub(test_data)
    poznan = hub.return_warehouse("Poznan Annex")
    if poznan is None:
        assert False
    assert len(poznan.to_be_given) == 0
    hub.start_request("Cracow Center", "Poznan Annex", "Apple", 3000)
    hub.skip_time()
    assert len(poznan.to_be_given) == 1


def test_proper_skipping_time_with_queeuing():
    hub = LogisticHub(test_data)
    hub.start_request("Poznan Annex", "Gdansk Port", "Orange", 400)
    hub.start_request("Warsaw Hub", "Gdansk Port", "Carrot", 2000)
    warehouse = hub.return_warehouse("Gdansk Port")
    if warehouse is None:
        return False
    assert len(hub.requests_list) == 2
    hub.skip_time()
    assert len(warehouse.to_be_given) == 1


def test_not_accepting_request_when_product_doesnt_exist():
    hub = LogisticHub(test_data)
    hub.start_request("Warsaw Hub", "Cracow Center", "Pear", 1)
    assert len(hub.requests_list) == 0


def test_removing_from_source_and_queue_in_destination():
    hub = LogisticHub(test_data)
    hub.start_request("Gdansk Port", "Lodz Depot", "Onion", 600)
    hub.skip_time()

    gdansk = hub.return_warehouse("Gdansk Port")
    lodz = hub.return_warehouse("Lodz Depot")

    onions_in_gdansk = False
    onions_in_lodz = False

    if gdansk is None or lodz is None:
        assert False

    for product in gdansk.curr_capacity:
        if product["product_name"] == "Onion":
            onions_in_gdansk = True
            break
    assert not onions_in_gdansk

    for product in lodz.curr_capacity:
        if product["product_name"] == "Onion":
            onions_in_lodz = True
            break
    assert not onions_in_lodz

    hub.remove_product("Lodz Depot", "Strawberry", 1000)
    hub.skip_time()

    for product in lodz.curr_capacity:
        if product["product_name"] == "Onion":
            onions_in_lodz = True
            break
    assert onions_in_lodz


def test_adding_existing_product_increases_quantity():
    hub = LogisticHub(test_data)
    hub.add_product("Warsaw Hub", "Banana", 50)
    hub.add_product("Warsaw Hub", "Banana", 30)

    warehouse = hub.return_warehouse("Warsaw Hub")
    quantity = 0
    if warehouse:
        for product in warehouse.curr_capacity:
            if product["product_name"] == "Banana":
                quantity = product["product_quantity"]

    assert quantity == 80


def test_deletion_of_unrealistic_request_after_save():
    hub = LogisticHub(test_data)
    hub.start_request("Warsaw Hub", "Lodz Depot", "Carrot", 400)
    warehouse = hub.return_warehouse("Lodz Depot")
    quantity = 0
    if not warehouse:
        return False
    for product in warehouse.curr_capacity:
        if product["product_name"] == "Carrot":
            quantity = product["product_quantity"]
    assert quantity == 1700
    assert len(hub.requests_list) == 1
    hub.skip_time()
    hub.save_hub()
    hub.load_hub()

    warehouse = hub.return_warehouse("Lodz Depot")
    if warehouse is None:
        return False
    hub.remove_product("Lodz Depot", "Strawberry", 1000)
    hub.skip_time()

    for product in warehouse.curr_capacity:
        if product["product_name"] == "Carrot":
            quantity = product["product_quantity"]
    assert quantity == 1700
    hub.add_product("Warsaw Hub", "Carrot", 400)
    hub.add_product("Lodz Depot", "Strawberry", 1000)
    hub.save_hub()


def test_queueing_requests_in_one_warehouse():
    hub = LogisticHub(test_data)
    hub.start_request("Poznan Annex", "Gdansk Port", "Orange", 400)
    hub.start_request("Warsaw Hub", "Gdansk Port", "Tomato", 300)
    hub.start_request('Cracow Center', "Gdansk Port", "Apple", 2000)
    gdansk = hub.return_warehouse("Gdansk Port")
    if gdansk is None:
        return False
    assert len(hub.requests_list) == 3
    hub.skip_time()
    assert len(gdansk.to_be_given) == 1


def test_receiving_requests_after_making_more_space():
    hub = LogisticHub(test_data)
    hub.start_request("Lodz Depot", "Cracow Center", "Carrot", 1000)
    hub.start_request("Warsaw Hub", "Cracow Center", "Carrot", 1000)
    hub.start_request("Poznan Annex", "Cracow Center", "Cucumber", 200)
    assert len(hub.requests_list) == 3
    cracow = hub.return_warehouse("Cracow Center")
    if cracow is None:
        return False

    hub.skip_time()
    assert len(cracow.to_be_given) == 2
    hub.remove_product("Cracow Center", "Apple", 1000)

    hub.skip_time()
    assert len(cracow.to_be_given) == 1
    hub.remove_product("Cracow Center", "Apple", 1000)

    hub.skip_time()
    assert cracow.curr_capacity[0]["product_quantity"] == 1000
    assert cracow.curr_capacity[1]["product_quantity"] == 2000
    assert cracow.curr_capacity[2]["product_quantity"] == 200
