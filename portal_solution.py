# I have no idea what problem this code is trying to solve 

def category_total(inventory, categories, category):
    count = 0
    for i in enumerate(inventory):
        count += 1
    return count

inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3}
categories = {"meat": ["bacon", "sausages", "steaks"],
             "fruit": ["bananas", "apples", "oranges", "peaches"]}
category = "fruit"

print(category_total(inventory, categories, category)) # 18