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

def check_points():
    print("Check points total")

def habits_list(file_name):
    print("Check habits tracked")
    with open(file_name, "r", newline='') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            print(row)

def remove_habit():
    print("Remove habit")