# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []
def display_menu():
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1
    return menu_items
def display_items(menu_category_name, menu_items):
    i = 1
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in menu[menu_category_name].items():
        if type(value) is dict:
            for key2, value2 in value.items():
                num_item_spaces = 24 - len(key + key2) - 3
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                menu_items[i] = {
                    "Item name": key + " - " + key2,
                    "Price": value2
                }
                i += 1
        else:
            num_item_spaces = 24 - len(key)
            item_spaces = " " * num_item_spaces
            print(f"{i}      | {key}{item_spaces} | ${value}")
            menu_items[i] = {
                "Item name": key,
                "Price": value
            }
            i += 1
def main():
    print("Welcome to the variety food truck.")
    place_order = True
    while place_order:
        menu_items = display_menu()
        menu_category = input("Type menu number: ")
        if menu_category.isdigit():
            if int(menu_category) in menu_items.keys():
                menu_category_name = menu_items[int(menu_category)]
                print(f"You selected {menu_category_name}")
                i = 1
                menu_items = {}
                display_items(menu_category_name, menu_items)
                menu_item_number = input("Enter the item number you'd like to order: ")
                if menu_item_number.isdigit():
                    menu_item_number = int(menu_item_number)
                    if menu_item_number in menu_items.keys():
                        selected_item = menu_items[menu_item_number]["Item name"]
                        while True:
                            quantity = input(f"How many {selected_item} would you like to order? ")
                            if quantity.isdigit():
                                quantity = int(quantity)
                            else:
                                quantity = 1
                            order_list.append({
                                "Item name": selected_item,
                                "Price": menu_items[menu_item_number]["Price"],
                                "Quantity": quantity
                                })
                            break
                    else:
                        print("Invalid menu item number")
                else:
                    print("Invalid input. Please enter a number.")
            else:
                print(f"{menu_category} was not a menu option.")
        else:
            print("You didn't select a number.")
        while True:
            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").upper()
            if keep_ordering == "N":
                place_order = False
                break
            elif keep_ordering == "Y":
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
    # Calculate the total cost of the order
    total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
    print("This is what we are preparing for you.\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for item in order_list:
        item_name = item["Item name"]
        item_price = item["Price"]
        item_quantity = item["Quantity"]
        num_item_spaces = 24 - len(item_name)
        item_spaces = " " * num_item_spaces
        print(f"{item_name}{item_spaces}| ${item_price:.2f} | {item_quantity}")
    print("\nTotal Cost: $", total_cost)
if __name__ == "__main__":
    main()