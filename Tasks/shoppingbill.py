Shoppinglist={'Samsung': 20000, 'Apple': 50000, 'Oneplus': 30000, 'Redmi': 15000,'Vivo': 25000, 'Oppo': 22000, 'Realme': 18000, 'Motorola': 28000, 'Nokia': 12000, 'LG': 35000}
print("Available items in the shopping list:")
for item, price in Shoppinglist.items():
    print(f"{item}: ${price}")
ShoppingCart=[]
while True:
    items = input("Enter the item you want to buy (or type 'done' to finish): ")
    if items == 'done':
        break
    if items in Shoppinglist:
        print(f"Price of {items}: ${Shoppinglist[items]}")
        ShoppingCart.append(items)
    else:
        print("Item not found in the shopping list.")

Total = sum(Shoppinglist[item] for item in ShoppingCart)
print(f"Total cost of items in the shopping cart: ${Total}")