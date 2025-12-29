from logistic_hub import LogisticHub
start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(test_data)
    hub.draw_graph()
