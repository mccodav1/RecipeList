# JT'sDinner
# Dave's easy solution to creating dinner menus and aggregating ingredients!
# Written 1/20/2020 by David McConnell

import os
import random

exitNum = 6  # Enter number of menu choices here, the last of which telling program to exit.


def welcome():
    print("Recipe / Buy List Producer, written by David McConnell. Last modified 1/19/2020")


def get_menu_choice():
    while True:
        try:
            choice = int(input('Select how to continue:\n1)\tAdd recipes to recipe list by name.\n2)\tAdd a selected '
                               'number of random recipes to recipe list.\n3)\tDelete item from recipe list.\n4)\tView '
                               'recipe list.\n5)\tClear recipe list to start over.\n6)\tSave recipe list '
                               '[RecipeList.txt] and quit application.'))
            if choice-1 in range(6):
                return choice
            else:
                print('Invalid entry; outside range. Enter 1 through 6.')
        except ValueError:
            print('Invalid entry; NaN. Enter 1 through 6.')


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
                input('\nCancelling. Press ENTER to return.\n')
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


def save_recipe_list(recipe_dict):
    ingredientDict = {}
    for item in recipe_dict:
        multiplier = recipe_dict[item]
        filename = item + '.txt'
        filepath = os.path.join(r'C:\Users\mccod\Documents\Python Projects\RecipeList\Recipes', filename)
        with open(filepath, 'r') as inputFile:
            line = inputFile.readline()
            while line:
                line = line.rstrip()
                qty = int(line)
                line = inputFile.readline()
                line = line.rstrip()
                ingredient = line.title()
                if ingredient in ingredientDict:
                    if multiplier == 0:
                        print('warning: multiplier = 0')
                    ingredientDict[ingredient] += qty * multiplier
                else:
                    if multiplier == 0:
                        print('warning: multiplier = 0')
                    ingredientDict[ingredient] = qty * multiplier
                line = inputFile.readline()
    filepath = os.path.join(r'C:\Users\mccod\Documents\Python Projects\RecipeList\RecipeList.txt')
    with open(filepath, 'w') as outputFile:
        for item in ingredientDict:
            outputFile.write(str(ingredientDict[item]))
            outputFile.write('\t')
            outputFile.write(item)
            outputFile.write('\n')
        # write recipe dict key and values, line by line
        outputFile.write('\nIngredients above to create:\n\n')
        for item in recipe_dict:
            outputFile.write(item)
            outputFile.write(': ')
            outputFile.write(str(recipe_dict[item]))
            outputFile.write('\n')


def add_items_to_dict(recipes_to_add, recipe_dict):
    recipesToAdd = list(filter(None, recipes_to_add))  # Get rid of none values
    recipesToAdd.sort()  # Sort alphabetically for readability
    for item in recipes_to_add:  # Iterate through list of recipes to add
        if item in recipe_dict:  # Check if item in recipeDict
            recipe_dict[item] += 1  # Add one to recipedict
    return recipe_dict


def delete_entry(recipe_dict):  # This is set t remove the key from dict. We don't want this. We want to make value=0
    recipeDictToList = []
    print("\nSelection: Delete item from recipe list.\n")
    print("Existing menu choices:")
    index = 1
    for item in recipe_dict:
        if not recipe_dict[item] == 0:
            print(index, ":\t", item)
            recipeDictToList.append(item)
            index += 1
    print('\nSelect a menu choice to delete it from menu list, or press 0 to cancel and return to menu:\n')
    delete = -1
    while delete not in range(len(recipeDictToList)+1):
        try:
            delete = int(input())
            if delete not in range(len(recipeDictToList)+1):
                print('\nInvalid entry: Not in range. Try again.\n')
        except ValueError:
            print('\nInvalid entry: ValueError. Try again.\n')
    if delete == 0:
        print('\nCancelling. Nothing deleted.\n')
        return recipe_dict
    else:
        keyToResetToZero = recipeDictToList[delete-1]
        recipe_dict[keyToResetToZero] = 0
        print('\nDeleting', keyToResetToZero, 'from list and returning to menu.\n')
        return recipe_dict


def main():
    menuChoice = 0
    welcome()
    availableRecipes = get_available_recipes()
    recipeDict = {i: 0 for i in availableRecipes}  # Dict of available recipes

    while not menuChoice == exitNum:  # Options 1 through 5; 5 saves and quits.
        recipesToAdd = []
        menuChoice = get_menu_choice()  # See what user wants to do

        if menuChoice == 1:  # Add recipe by name
            recipesToAdd.append(add_recipe_by_name(availableRecipes))
            recipeDict = add_items_to_dict(recipesToAdd, recipeDict)

        elif menuChoice == 2:
            randomRecipes = add_random_recipes(availableRecipes)
            if randomRecipes:
                for item in randomRecipes:
                    recipesToAdd.append(item)
                recipeDict = add_items_to_dict(recipesToAdd, recipeDict)

        elif menuChoice == 3:
            recipeDict = delete_entry(recipeDict)

        elif menuChoice == 4:
            print('\nRecipe list:\n')
            if all(x == 0 for x in recipeDict.values()):
                print('No recipes in list!\n')
            else:
                for item in recipeDict:
                    if recipeDict[item] > 0:
                        print('\t', item, '\t', recipeDict[item], end='\n')
                print('\n')

        elif menuChoice == 5:  # Clear recipe list
            for item in recipeDict:
                recipeDict[item] = 0
            input('\nClearing recipe list to start over. Press ENTER to return to menu.\n')

    finalDict = {}
    for item in recipeDict:
        if recipeDict[item] > 0:
            finalDict[item] = recipeDict[item]
    save_recipe_list(finalDict)  # Save recipe list to RecipeList.txt
    input('Recipe list saved to RecipeList.txt. Press ENTER to exit.')  # 5 entered; save and quit.


main()

