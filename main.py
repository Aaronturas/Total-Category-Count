def category_total(inventory, categories, category):
  # Keep track of the total number of items for a specific category
  num = 0
  
  # Iterate through the items in the category
    # Add the count for each item to the total
  for i in categories[category]:
    num += inventory.get(i, 0)
    
  # Return the total
  return num

#test cases
inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3}
categories = {"meat": ["bacon", "sausages", "steaks"],
             "fruit": ["bananas", "apples", "oranges", "peaches"]}
category = "fruit"
print('Inventory:',inventory)
print('Categories:',categories)
print('Category:',category)
print('The number of items in the', category, 'category is',category_total(inventory, categories, category), '\n') # 18

inventory = {"bananas": 5, "apples": 3, "oranges": 10, "bacon": 1, "sausages": 3, "melons":"6", "cheese": 4, "milk":7}
categories = {"meat": ["bacon", "sausages", "steaks"],
             "fruit": ["bananas", "apples", "oranges", "peaches"], "dairy": ["cheese","milk"]}
category = "dairy"
print('Inventory:',inventory)
print('Categories:',categories)
print('Category:',category)
print('The number of items in the', category, 'category is',category_total(inventory, categories, category), '\n') # 11
