fruit_stock = {
    "Apple":{"price":20, "quantity":30},
    "Orange":{"price":30, "quantity":40},
    "Grapes":{"price":40, "quantity":50}
}

def show_fruit():
    for fruit in fruit_stock:
        print("fruit:",fruit)
        print("price:",fruit_stock[fruit]["price"])
        print("quantity:",fruit_stock[fruit]["quantity"])
        print("--------------------------------")
    
def add_fruit():
    name = input("enter fruit name:")
    price = int(input("enter the price of fruit:"))
    quantity = int(input("enter the quantity of fruit:"))
    fruit_stock[name]={"price": price, "quantity":quantity}
    print("fruit added:")
    print("--------------------")
    
def update_quantity():
    name = input("enter fruits name:")
    if name in fruit_stock:
        new_quantity = int(input("enter new quantity:"))
        fruit_stock[name]["quantity"] = new_quantity
        print("quantity updated:")
    else:
        print("quantity failed")
    print("----------------------")
    
while True:
    print("1. show_fruit:")
    print("2. add_fruit:")
    print("3. update_fruit:")
    print("4. exit:")
     
    choice = input("enter your choice:")
     
    if choice == "1":
        show_fruit()
    elif choice == "2":
        add_fruit()
    elif choice == "3":
        update_quantity()
    elif choice == "4":
        print("exit")
        break
    else:
        print("not updated")