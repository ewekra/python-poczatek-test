
products = {
    "chleb": {
        "quantity": 100,
        "prise": 3.5
    },
    "jabłka": {
        "quantity": 50,
        "prise": 3.2
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity