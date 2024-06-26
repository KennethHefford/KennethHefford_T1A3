# System packages
import os.path

# External packages
from colored import Fore, Back, Style
import emoji

# Imports of created functions

from application_functions import add_good, add_bad, check_points, habits_list, remove_habit
print(f"{Fore.blue}Welcome to the good habits tracker application!{Style.reset}")

# Menu
def create_menu():

    print("1. Enter 1 to add good habit to the list")
    print("2. Enter 2 to add bad habit to the list")
    print("3. Enter 3 to check Total Points today")
    print("4. Enter 4 View habits tracked today")
    print("5. Enter 5 to Remove a habit")
    print("6. Enter 6 to exit")

    user_choice = input(f"{Fore.blue}Enter your selection: {Style.reset}")
    return user_choice

file_name = "list.csv"

# check if file does not exist
if (not os.path.isfile(file_name)):
    print("Creating habits list file")
    # create the file
    habits_file = open(file_name, "w")
    # enter the headings into the file
    habits_file.write("habit,count\n")
    # close the file
    habits_file.close()

choice = ""

# Function for menu choices
while choice != "6":
    choice = create_menu()

    if (choice == "1"):
        add_good(file_name)
    elif (choice == "2"):
        add_bad(file_name)
    elif (choice == "3"):
        check_points(file_name)
    elif (choice == "4"):
        habits_list(file_name)
    elif (choice == "5"):
        remove_habit(file_name)
    elif (choice == "6"):
        print("You entered 6.")
    else:
        print(f"{Fore.red}Please enter from the options available 1-6.{Style.reset}")



# Thank you message
print(emoji.emojize(f"{Back.blue}Thankyou for using the good habits tracker application!:thumbsup: {Style.reset}", language='alias'))