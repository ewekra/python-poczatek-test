from sklep.orders import new_order

product = input("Co chcesz zamówić? ")
quantity = input("W jakiej ilości? ")

print(f"(Twoje zamówienie -> {product}, {quantity}, cena: {quantity * product_price})