from logistic_hub import LogisticHub

start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(start_data)
    print("--------------------------")
    print("-------Logistic Hub-------")
    print("--------------------------")
    print("-What do you want to do?--")
    print()
    print("1. See warehouses on a graph")
    print("2. Add product to a warehouse")
    print("3. Remove product from a warehouse")
    print("4. Look for a specific product across hub")
    print("5. Look what specific warehouse has")
    print("6. Start request")
    print("7. Save hub to file")
    print("Other options: Exit")
    choice = input()

    match choice:
        case "1":
            hub.draw_graph()
        case _:
            print("Thanks for using that programme!")