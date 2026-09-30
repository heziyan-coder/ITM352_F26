# determine how busy the Ramen restaurant is based on the number of orders


test_orders = [
    ["miso", "shoyu"],
    ["miso", "shoyu", "spicy", "tonkotsu", "miso", "shoyu"],
    ["miso", "shoyu", "spicy", "tonkotsu", "miso", "shoyu",
     "spicy", "miso", "shoyu", "tonkotsu", "miso", "spicy"]
]
for orders in test_orders:
    if len(orders) < 5:
        print("not busy")
    elif 5 <= len(orders) <= 10:
        print("busy")
    else:
        print ("very busy")