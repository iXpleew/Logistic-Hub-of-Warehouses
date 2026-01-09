from logistic_hub import LogisticHub
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


def test_connection():
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
        if warehouse.name != "Warsaw Hub":
            current_warehouse = warehouse
            break
    assert current_warehouse is not None


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


# def test_negative_values_handling():
#     hub = LogisticHub(test_data)

#     assert hub.add_product("Warsaw Hub", "ErrorItem", -50) is False

#     assert hub.remove_product("Warsaw Hub", "Carrot", -10) is False
