def check_budget(recent_purchase,budget):
    for purchase in recent_purchase:
        if purchase > budget:
            print( "This purchase is over budget!")
        else:
            print("This purchase is within budget")