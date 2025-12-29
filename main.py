from logistic_hub import LogisticHub
start_data = "data.json"

if __name__ == "__main__":
    hub = LogisticHub(start_data)
    hub.add_warehuse(
        name="Wroclaw Hub",
        max_capaci=2000,
        curr_capaci=[
            {
                "product_name": "Cucumber",
                "product_quantity": 1900
            }
        ],
        connections=[{
            "target_name": "Cracow Center",
            "distance": 100
        }]
    )
    hub.draw_graph()
