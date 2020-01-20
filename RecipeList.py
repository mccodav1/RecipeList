# Features:
# 1) Add recipes to buy list by name
# 2) Randomly select X recipes and add items to recipe list
# 3) View recipe list with list of ingredients to buy

import os
import random


def welcome():
    print("Recipe / Buy List Producer, written by David McConnell. Last modified 1/19/2020")


def get_menu_choice():
    while True:
        try:
            choice = int(input('Select how to continue:\n1)\tAdd recipes to recipe list by name.\n2)\tAdd a selected '
                               'number of random recipes to recipe list.\n3)\tView recipe list.\n4)\tClear recipe list '
                               'to start over.\n5)\tSave recipe list [RecipeList.txt] and quit application.'))
            if choice in range(0, 6):
                return choice
            else:
                print('Invalid entry. Enter 1 through 5')
        except ValueError:
            print('Invalid entry. Enter 1 through 5')


def get_available_recipes():
    path = r"C:\Users\mccod\Documents\Python Projects\RecipeList\Recipes"
    availableRecipes = ['.'.join(x.split('.')[:-1]) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    return availableRecipes


def add_recipe_by_name(available_recipes):
    print("\nSelection: Add recipes to recipe list by name.\n")
    while True:
        print("Available recipes:\n")
        for item in available_recipes:
            print(available_recipes.index(item)+1, ")\t", item, sep='')
        print("\nWhich recipe would you like to add? Enter its number and press ENTER to add.")

        try:
            recipeToAdd = int(input())
            if recipeToAdd in range(1, len(available_recipes) + 1):
                recipeToAdd -= 1
                print('You selected', available_recipes[recipeToAdd], 'which will be added to your recipe list.\n')
                return available_recipes[recipeToAdd]
            else:
                print("\nInvalid Entry. Enter a number from the get_menu_choice.\n")
        except ValueError:
            print("\nInvalid Entry. Enter a number from the get_menu_choice.\n")


def add_random_recipes(available_recipes):
    print("\nSelection: Add a selected number of random recipes to recipe list.\n")
    while True:
        try:
            print('Number of current recipes in database:', len(available_recipes))
            numberToAdd = int(input('Enter the number of recipes you wish to randomly add, or 0 to cancel:'))
            if numberToAdd > len(available_recipes):
                print('Warning: You are attempting to add more recipes than exist in the database. This will cause '
                      'recipes to be duplicated. Continue? Y/N:')
                acceptWarning = input()
                if not acceptWarning.upper() == 'Y':
                    input('\nCanceling random input of recipes. Returning to main menu. Press ENTER to continue.\n')
                    return
                else:
                    print('Adding', numberToAdd, 'random recipes...\n') # get random recipes
                    randomRecipes = get_random_recipes(available_recipes, numberToAdd)
                    return randomRecipes
            elif numberToAdd < 0:
                print('\nInvalid entry. You must enter a number. Input 0 to cancel.\n')
            elif numberToAdd == 0:
                print('\nCancelling. Press ENTER to return.\n')
                return
            else:
                print('Adding', numberToAdd, 'random recipes...\n')  # get random recipes
                randomRecipes = get_random_recipes(available_recipes, numberToAdd)
                return randomRecipes
        except ValueError:
            print('\nInvalid entry: ValueError.\n')


def get_random_recipes(available_recipes, num):
    randomRecipes = []

    if num < len(available_recipes):  # Adding less recipes than exist. Get random sample, without duplicates.
        indexesToAdd = random.sample(range(0, len(available_recipes)), num)

    else: # Adding same number or more recipes than exist in database. Randomly add recipes.
        indexesToAdd = []
        for number in range(0, num):
            indexesToAdd.append(random.randint(0, len(available_recipes)-1)) # Now I have a list of indexes of recipes
        for item in indexesToAdd:
            randomRecipes.append(available_recipes[item])
    return randomRecipes

def view_recipe_list():
    # to do
    return


def save_recipe_list():
    return


def main():
    availableRecipes = get_available_recipes()
    recipesToAdd = []
    menuChoice = 0
    welcome()
    while not menuChoice == 5:
        menuChoice = get_menu_choice()
        if menuChoice == 1:
            recipesToAdd.append(add_recipe_by_name(availableRecipes))
            recipesToAdd = list(filter(None, recipesToAdd))
            recipesToAdd.sort()
        elif menuChoice == 2:
            randomRecipes = add_random_recipes(availableRecipes)
            for item in randomRecipes:
                recipesToAdd.append(item)
            recipesToAdd = list(filter(None, recipesToAdd))
            recipesToAdd.sort()
        elif menuChoice == 3:
            print('\nRecipe list:', end='\n')
            for item in recipesToAdd:
                print('\t', item, end='\n')
    # Add a selected number of random recipes to recipe list.
    # save recipe list
    input('Recipe list saved to RecipeList.txt. Press ENTER to exit.')

main()

