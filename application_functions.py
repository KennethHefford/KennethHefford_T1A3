import csv


def add_good(file_name):
    print("Add Good Habit")
    good_name = input("Enter a Good Habit: ")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([good_name, 1])


def add_bad(file_name):
    print("Add Bad Habit")
    bad_name = input("Enter a Bad Habit: ")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([bad_name, -1])

def check_points(file_name):
    print("Check points total")
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            total_points = (sum([1]))
            print(total_points)

def habits_list(file_name):
    try:
        print("Check habits for today")
        with open(file_name, "r", newline='') as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                print(row [0])
    except FileNotFoundError:
        print("The habits list does not exist")

def remove_habit(file_name):
    good_habit, bad_habit = input("Enter which habit you would like to remove: ")
    current_list = []
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        existing_habit = False
        for row in reader:
            if (good_habit, bad_habit != row[0]):
                good_habit.append(row)
                bad_habit.append(row)
            else:
                existing_habit = True
    if not existing_habit:
        print("Habit has not been added.")
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(current_list)