from logistic_hub import LogisticHub
import pytest

invalid_data = "invalid_data.json"
valid_data = "data.json"


def test_creating_logistic_hub():
    _ = LogisticHub(valid_data)


def test_maximum_capacity_overreached():
    with pytest.raises(ValueError):
        _ = LogisticHub(invalid_data)


def test_adding_new_overreached_hub():
    with pytest.raises(ValueError):
        hub = LogisticHub(valid_data)
        hub.add_warehouse(
            name="Wroclaw Hub",
            max_capaci=2000,
            curr_capaci=[
                {
                    "product_name": "Cucumber",
                    "product_quantity": 123900
                }
            ],
            connect=[{
                "target_name": "Cracow Center",
                "distance": 100
            }]
        )


def test_return_correct_data_file():
    hub = LogisticHub(valid_data)
    assert valid_data == hub.data_file


def test_crating_new_warehouse():
    # There are 5 hubs in valid data
    hub = LogisticHub(valid_data)
    assert len(hub.ware_list) == 5
    hub.add_warehouse("Wroclaw Hub", 20, curr_capaci=None, connect=None)
    assert len(hub.ware_list) == 6


def test_looking_for_warehouse():
    hub = LogisticHub(valid_data)
    current_warehouse = None
    for warehouse in hub.ware_list:
        if warehouse.name != "Warsaw Hub":
            current_warehouse = warehouse
            break
    assert current_warehouse is not None
