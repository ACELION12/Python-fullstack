products = {'tv':45000,'camera':15000,'laptop':68000,'ac':52000}
new_products = {product: price for product, price in products.items() if price < 50000}
new_Hproducts = {product: price - price * 5 // 100 for product, price in products.items() if price > 50000}
final_products = {**new_products, **new_Hproducts}
print (new_products)
print (new_Hproducts)
print(final_products)
