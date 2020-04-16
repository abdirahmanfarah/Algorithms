#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # two dict args
    # num_of_recipes variable
    num_of_recipes = 0
    # first loop is to check values of recipe
    for key, value in recipe.items():
        # if statement where value of *all ingredients is more than the value of *all recipes
      for key, value in ingredients.items():
        y = recipe[key]
        x = ingredients[key]
          # print(x, y)
        if x > y:
                # print ('ingredients[key]')
          num_of_recipes +=1

        else:   
          num_of_recipes
    return num_of_recipes


# recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {
#     'milk': 5, 'sugar': 120, 'butter': 500})

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
