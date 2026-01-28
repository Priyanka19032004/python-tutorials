fruit_stock = {
    "Apple":{"price":10,"quantity":5},
    "Orange":{"price":20,"quantity":4},
    "Papaya":{"price":30,"quantity":3}
    }
print("--------------------")
total_value = 0
for fruit_name in fruit_stock:
    fruit_price = fruit_stock[fruit_name]["price"]
    fruit_quantity = fruit_stock[fruit_name]["quantity"]
    fruit_value = fruit_price * fruit_quantity
    total_value = total_value + fruit_value
    print("fruit:",fruit_name)
    print("price:",fruit_price)
    print("quantity:",fruit_quantity)
    print("value:",fruit_value)
    print("-------------------")
print("total price of all fruit:",total_value)