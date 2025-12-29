from logistic_hub import LogisticHub
import pytest

invalid_data = "invalid_data.json"
valid_data = "data.json"


def test_creating_logistic_hub():
    _ = LogisticHub(valid_data)


def test_maximum_capacity_overreached():
    with pytest.raises(ValueError):
        _ = LogisticHub(invalid_data)
