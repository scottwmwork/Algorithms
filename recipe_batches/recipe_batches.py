#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = 0
  first_val = list(ingredients.values())[0] // list(recipe.values())[0] 
  current_min = []
  for ing in recipe:
    #Check if ingredient is available
    if ing not in ingredients or ingredients[ing] < recipe[ing]:
      return 0 
    val = ingredients[ing] // recipe[ing]
    
    if count == 0:
      current_min.append(val)
    elif val < current_min[len(current_min) - 1]:
      current_min.append(val)
    
    count += 1 

    
  batch_size = current_min[len(current_min) - 1]   
  return batch_size

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'cheese': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'cheese': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))