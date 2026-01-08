from logistic_hub import LogisticHub

start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(start_data)
    hub.show_what_warehouse_has("Warsaw Hub")
    hub.add_product("Warsaw Hub", "Carrot", 3000)
    hub.show_what_warehouse_has("Warsaw Hub")
    hub.start_request("Warsaw Hub", "Poznan Annex", "Carrot", 10)
    hub.show_actual_requests()
    hub.draw_graph()

    # remember to reduce number of product that are sent to warehouse
    # when request has
