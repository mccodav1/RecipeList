# Features:
# 1) Add recipes to buy list by name
# 2) Randomly select X recipes and add items to recipe list
# 3) View recipe list with list of ingredients to buy

import os

def welcome():
    print("Recipe / Buy List Producer")


def menu():
    while True:
        try:
            choice = int(input("Select how to continue:\n1)\tAdd recipes to recipe list by name.\n2)\tAdd a selected "
                               "number of random recipes to recipe list.\n3)\tView recipe list.\n4)\tSave recipe list "
                               "[RecipeList.txt] and quit application."))
            if choice in range(0, 5):
                return choice
            else:
                print('Invalid entry. Enter 1 through 4')
        except ValueError:
            print('Invalid entry. Enter 1 through 4')


def get_available_recipes():
    path = r"C:\Users\mccod\Documents\Python Projects\RecipeList\Recipes"
    availableRecipes = ['.'.join(x.split('.')[:-1]) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    return availableRecipes


def add_recipe_by_name():
    print("\nSelection: Add recipes to recipe list by name.\n")
    availableRecipes = (get_available_recipes())
    while True:
        print("Available recipes:\n")
        for item in availableRecipes:
            print(item)
        print("\nWhich recipe would you like to add? Enter its number and press ENTER to add.")

        try:
            recipeToAdd = int(input())
            if recipeToAdd in range(1, len(availableRecipes)+1):
                recipeToAdd -= 1
                print('You selected', availableRecipes[recipeToAdd], 'which will be added to your recipe list.\n')
                return
            else:
                print("\nInvalid Entry. Enter a number from the menu.\n")
        except ValueError:
            print("\nInvalid Entry. Enter a number from the menu.\n")





def add_number_of_recipes():
    # to do
    return

def view_recipe_list():
    # to do
    return

def save_recipe_list():
    return


def main():
    menuChoice = 0
    welcome()
    while not menuChoice == 4:
        menuChoice = menu()
        if menuChoice == 1:
            add_recipe_by_name()
    # save recipe list
    input('Recipe list saved to RecipeList.txt. Press ENTER to exit.')

main()

