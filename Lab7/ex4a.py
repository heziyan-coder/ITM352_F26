recent_purchase = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 50
total_spent = 0

for purchase in recent_purchase:
    if purchase > budget:
        print(f"This purchase is over budget!")
    else:
        print(f"This purchase is within budget")