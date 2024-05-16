import csv
from colored import Fore, Back, Style

def add_good(file_name):
    print("Add Good Habit")
    good_name = input(f"{Fore.blue}Enter a Good Habit: {Style.reset}")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([good_name, 1])


def add_bad(file_name):
    print("Add Bad Habit")
    bad_name = input(f"{Fore.red}Enter a Bad Habit: {Style.reset}")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([bad_name, -1])

def check_points(file_name):
    print(f"{Fore.green}Check points total{Style.reset}")
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        reader.__next__()
        total_points = 0
        for row in reader:
            total_points = total_points + int(row[-1])
    print(total_points)

def habits_list(file_name):
    try:
        print(f"{Fore.green}Check habits for today {Style.reset}")
        with open(file_name, "r", newline='') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                print(row [0])
    except FileNotFoundError:
        print(f"{Fore.red}The habits list does not exist{Style.reset}")

def remove_habit(file_name):
    habit_name = input("Enter which habit you would like to remove: ")
    current_list = []
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        habit_name = False
        for row in reader:
            if (habit_name!= row):
                habit_name.append(row)
            else:
                habit_name = True
    if not habit_name:
        print("Habit has not been added already.")
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(current_list)