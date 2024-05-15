# System packages
import os.path

# External packages
# from colored import Fore, Back, Style


# Imports of created functions

from application_functions import add_good, add_bad, check_points, habits_list, remove_habit
print("Welcome to the good habits tracker application")

def create_menu():

    print("1. Enter 1 to add good habit to the list")
    print("2. Enter 2 to add bad habit to the list")
    print("3. Enter 3 to check Total Points today")
    print("4. Enter 4 View habits tracked today")
    print("5. Enter 5 to Remove a habit")
    print("6. Enter 6 to exit")

    user_choice = input("Enter your selection: ")
    return user_choice

file_name = "list.csv"

# check if file does not exist
if (not os.path.isfile(file_name)):
    print("Creating habits list file")
    # create the file
    habits_file = open(file_name, "w")
    # we will enter the headings into the file
    habits_file.write("habit,count\n")
    # close the file
    habits_file.close()

choice = ""


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
        print("Please enter from the options available 1-6.")




print("Thankyou for using the good habits tracker application!")