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
