from logistic_hub import LogisticHub
start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(test_data)
    hub.add_warehouse(
        name="Wroclaw Hub",
        max_capaci=2000,
        curr_capaci=[
            {
                "product_name": "Cucumber",
                "product_quantity": 1900
            }
        ],
        connect=[{
            "target_name": "Cracow Center",
            "distance": 100
        }]
    )
    hub.draw_graph()
