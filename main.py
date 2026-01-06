from logistic_hub import LogisticHub

start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(start_data)
    hub.show_what_warehouse_has("Warsaw Hub")
    hub.add_product("Warsaw Hub", "Carrot", 3000)
    hub.save_hub()
