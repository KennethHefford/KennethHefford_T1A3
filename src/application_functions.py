# System Packages
import csv

# External Packages
from colored import Fore, Back, Style
import emoji

# Adding a Good Habit

def add_good(file_name):
    print(emoji.emojize("Good Habit is one point :beaming_face_with_smiling_eyes:", language='alias'))
    good_name = input(f"{Fore.blue}Enter a Good Habit: {Style.reset}")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([good_name, 1])

# Adding a Bad Habit
def add_bad(file_name):
    print(emoji.emojize("Bad Habit is minus one point :upside_down_face:", language='alias'))
    bad_name = input(f"{Fore.red}Enter a Bad Habit: {Style.reset}")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([bad_name, -1])

# Check Total Points with Error Handling
def check_points(file_name):
    try:
        print(emoji.emojize(f"{Fore.green}Check points total - aim for 10 :smiling_face_with_open_hands:{Style.reset}", language='alias'))
        with open(file_name, "r", newline='') as f:
            reader = csv.reader(f)
            reader.__next__()
            total_points = 0
            for row in reader:
                total_points = total_points + int(row[-1])
    except FileNotFoundError:
        print(print(f"{Fore.red}The habits list does not exist{Style.reset}"))
    print(total_points)

    
# Check Habits List with Error Handling
def habits_list(file_name):
    try:
        print(emoji.emojize(f"{Fore.green}Check habits for today :check_mark: {Style.reset}", language='alias'))
        with open(file_name, "r", newline='') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                print(row [0])
    except FileNotFoundError:
        print(f"{Fore.red}The habits list does not exist{Style.reset}")

# Remove Habits List with Error Handling
def remove_habit(file_name):
    print(emoji.emojize(f"{Fore.green}Remove Habit :cross_mark:{Style.reset}", language='alias'))
    habit_name = input(f"{Fore.green}Enter which Habit you would like to remove: {Style.reset}")
    current_list = []
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        existing_habit = False
        for row in reader:
            if (habit_name!= row[0]):
                current_list.append(row)
            else:
                existing_habit = True
    if not existing_habit:
        print(f"{Fore.red}Habit has not been added yet.{Style.reset}")
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(current_list)