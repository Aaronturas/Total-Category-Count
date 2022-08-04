# Write the function category_total which gives the total number of items of a specific category. It takes the following as input:
# inventory: a dictionary where each key is an item and the value is the count
# categories: a dictionary where each key is a category and the value is a list of the items in that category
# category: a category (one of the keys of the categories dictionary)

# If an item from the category list isn’t in the inventory, assume the count is 0.

def category_total(inventory, categories, category):
  # Keep track of the total number of items for a specific category
  num = 0
  
  for i in categories[category]:
    num += inventory.get(i)

  return num
  # Iterate through the items in the category
    # Add the count for each item to the total

  # Return the total

inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3}
categories = {"meat": ["bacon", "sausages", "steaks"],
             "fruit": ["bananas", "apples", "oranges", "peaches"]}
category = "fruit"
print(category_total(inventory, categories, category)) # 18

inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3, "melons":"6", "yogurt":"4", "milk":"7"}
categories = {"meat": ["bacon", "sausages", "steaks"],
             "fruit": ["bananas", "apples", "oranges", "peaches"], "dairy": ["yogurt","milk"]}
category = "dairy"
print(category_total(inventory, categories, category)) # 18