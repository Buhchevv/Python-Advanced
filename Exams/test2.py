def shop_from_grocery_list(budget, grocery_list, *products):
    bought_items = set()
    missing_items = grocery_list
    total_cost = 0

    for item, price in products:
        if item in grocery_list and item not in bought_items and budget >= price:
            budget -= price
            bought_items.add(item)
            missing_items.remove(item)
            total_cost += price
        if not missing_items:
            return f"Shopping is successful. Remaining budget: {budget:.2f}."
    if missing_items:
        return f"You did not buy all the products. Missing products: {''.join(missing_items)}."
    return f"You spent all the budget: {total_cost:.2f}."


print(shop_from_grocery_list(

    100,

    ["tomato", "cola", "chips", "meat"],

    ("cola", 5.8),

    ("tomato", 10.0),

    ("meat", 22),

))