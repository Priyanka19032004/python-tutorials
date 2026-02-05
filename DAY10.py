fruit_inventary = {}
def load_fruit():
    try:
        with open("fruit.txt","r") as file:
            for line in file:
                if line.strip() == "":
                    name , price , quantity = line.strip().split(",")
        fruit_inventary [name] = {
            "price" == int(price),
            "quantity" == int(quantity)
        }
    except:
        print("no data found")
    
def save_data():
    with open("fruit.txt","w") as file:
        for fruit in fruit_inventary:
            price = fruit_inventary[fruit]["price"]
            quantity = fruit_inventary[fruit]["quantity"]

def view_fruit():
    if not fruit_inventary:
        print("inventary is empty")
        return
    
    print("\n==========FRUIT INVENTARY===============")
    for fruit in fruit_inventary:
        price = fruit_inventary[fruit]["price"]
        quantity = fruit_inventary[fruit]["quantity"]

        print("fruit",fruit)
        print("price",price)
        print("quantity",quantity)

        if quantity <= 10:
            print("low stock")

        print("-----------------------------")

def add_fruit():
    name = input("Enter fruit name: ")

    if name == "":
        print("Fruit name cannot be empty")
        return

    if name in fruit_inventary:
        print("Fruit already exists")
        return

    try:
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except:
        print("Price and quantity must be numbers")
        return

    fruit_inventary[name] = {"price": price, "quantity": quantity}
    save_data()
    print("Fruit added successfully")


def update_quantity():
    name = input("enter fruit name:")

    if name not in fruit_inventary:
        print("fruit not found")
        return
    
    try:
        new_qty = int(input("enter new quantity:"))
    except:
        print("quatity must be number")
        return
    
    fruit_inventary[name]["quantity"] = new_qty
    save_data()
    print("quantity updated")

def total_value():
    total = 0
    for fruit in fruit_inventory:
        total += fruit_inventory[fruit]["price"] * fruit_inventory[fruit]["quantity"]

    print("Total inventory value:", total)


    load_data()

while True:
    print("\n--- FRUIT INVENTORY SYSTEM ---")
    print("1. View Fruit")
    print("2. Add Fruit")
    print("3. Update Quantity")
    print("4. Total Inventory Value")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_fruit()
    elif choice == "2":
        add_fruit()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        total_value()
    elif choice == "5":
        print("Exiting program")
        break
    else:
        print("Invalid choice")