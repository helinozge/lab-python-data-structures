#   = ANSWER =


products = ["t-shirt","mug","hat","book","keychain"]
inventory =  {}

for product  in products:
    quantity = int(input(f"Enter quantity for {product}:"))
    inventory[product]  = quantity

customer_orders = set()

for i in range(3):
    while True:
        order  = input(f"Please enter the product {i+1}:").lower()
        if order in products:
            customer_orders.add(order)
        else:
            print("Invalid product. Please choose from the list.")

print("\nCustomer Orders:", customer_orders)

order_status = ("total_products_ordered","percentage_ordered")

total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered/len(products)) * 100

print("\nOrder Statistics:")
print(f"Total Products Ordered: {order_status[0]}")
print(f"Percentage of Products Ordered: {order_status[1]}%")

for product in customer_orders:
    if inventory[product] > 0:
        inventory[product]  -= 1

print("\nUpdated Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

