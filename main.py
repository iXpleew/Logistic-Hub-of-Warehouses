from logistic_hub import LogisticHub

start_data = "data.json"
test_data = "testing_data.json"

if __name__ == "__main__":
    hub = LogisticHub(test_data)
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
    print("7. Show requests")
    print("8. Skip time")
    print("9. Save hub")
    print("Other options: Exit")
    choice = input()

    match choice:
        case "1":
            hub.draw_graph()
        case "2":
            warehouse = input("To which warehouse to want to add something?").capitalize()
            product = input("What do you want to add?").capitalize()
            quantity = int(input("And how much?"))
            hub.add_product(warehouse, product, quantity)
        case "3":
            warehouse = input("From which warehouse to want to remove something?").capitalize()
            product = input("What do you want to remove?").capitalize()
            quantity = int(input("And how much?"))
            hub.remove_product(warehouse, product, quantity)
        case "4":
            product = input("What do you want to search across hub?").capitalize()
            hub.search_product(product)
        case "5":
            warehouse = input("Which warehouse you want to check?").capitalize()
            hub.show_what_warehouse_has(warehouse)
        case "6":
            source = input("From which warehouse you want to take product?").capitalize()
            target = input("To where?").capitalize()
            product = input("And what product?").capitalize()
            quantity = int(input("And how much?"))
            hub.start_request(source, target, product, quantity)
        case "7":
            hub.show_actual_requests()
        case "8":
            hub.skip_time()
        case "9":
            print("If you've made a deadlock while inserting your data")
            print("some requests may be cancelled and products will be reprocessed")
            print("due to bad managment")
            choice = input("Do you really want to save hub? Y/other").capitalize()
            if choice == "Y":
                hub.save_hub()
                hub.load_hub()
        case _:
            print("Thanks for using that programme!")
