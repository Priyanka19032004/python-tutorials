products = ["pen" , "pencil", "books"]
prices = [ 5, 10 , 15]
quantities = [ 20, 30 ,40]
total_value = 0

print("\n---------------------------")
print("      INVENTORY REPORT           ")
print("-------------------------------")

for i in range(len(products)):
    product = products[i]
    price = prices[i]
    quantity = quantities[i]
    item_value = price * quantity
    total_value = total_value + item_value

    print("product:",product)
    print("price:",price)
    print("quantity:",quantity)
    print("item_value:",item_value)
    print("------------------------")

print("==================================")
print("total inventory value:",total_value)
print("===================================")