from logistic_hub import LogisticHub
import os
import time

start_data = "data.json"
test_data = "testing_data.json"


def check_if_digit(string: str):
    if not string.isdigit():
        print("Entered valued has to be a positive Integer!")
        print("Order is cancelled!")
        time.sleep(2.5)
        return False
    else:
        return True


if __name__ == "__main__":
    hub = LogisticHub(test_data)
    while True:
        os.system("clear")
        print("--------------------------")
        print("-------Logistic Hub-------")
        print("--------------------------")
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
        choice = input("What do you want to do?: ")
        print()

        match choice:
            case "1":
                hub.draw_graph()
                input("Click anything to continue: ")
            case "2":
                warehouse = input("To which warehouse to want to add something?: ").strip().title()
                product = input("What do you want to add?: ").strip().title()
                quantity = input("And how much?: ")
                if check_if_digit(quantity):
                    hub.add_product(warehouse, product, int(quantity))
            case "3":
                warehouse = input("From which warehouse to want to remove something?: ").strip().title()
                product = input("What do you want to remove?: ").strip().title()
                quantity = input("And how much?: ")
                if check_if_digit(quantity):
                    hub.remove_product(warehouse, product, int(quantity))
            case "4":
                product = input("What do you want to search across hub?: ").strip().title()
                hub.search_product(product)
                input("Click anything to continue: ")
            case "5":
                warehouse = input("Which warehouse you want to check?: ").strip().title()
                hub.show_what_warehouse_has(warehouse)
                input("Click anything to continue: ")
            case "6":
                source = input("From which warehouse you want to take product?: ").strip().title()
                target = input("To where?: ").strip().title()
                product = input("And what product?: ").strip().title()
                quantity = input("And how much?: ")
                if check_if_digit(quantity):
                    hub.start_request(source, target, product, int(quantity))
            case "7":
                hub.show_actual_requests()
                input("Click anything to continue: ")
            case "8":
                hub.skip_time()
            case "9":
                print("If you've made a deadlock while inserting your data")
                print("some requests may be cancelled and products will be reprocessed")
                print("due to bad managment")
                choice = input("Do you really want to save hub? Y/other: ").strip().title()
                if choice == "Y":
                    hub.save_hub()
                    hub.load_hub()
            case _:
                print("Thanks for using that programme!")
                break
