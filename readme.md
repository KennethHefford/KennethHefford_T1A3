# Kenneth Hefford Terminal Application T1A3 - Habits Tracker

link to github repository: https://github.com/KennethHefford/KennethHefford_T1A3

link to project management platform: https://trello.com/b/EtSEOeou/t1a3

### System Packages used:
os.path
import csv

### External Packages used:
colored
emoji

## Coding Styling Conventions
The Styling Convention used to create this Terminal Application is PEP-8.

## Purpose of the Application
The purpose of the application is to allow the end user to track their habits whether good or bad. It is designed to help users cultivate positive habits, stay accountable, and foster mindfulness. The application will have a menu list that will correspond which each feature such as adding a habit or closing the application. The user will enter a number (1-6) that coincides with a menu item to input or activate a feature.

## Features of the Application

### 1. Positive Habit Accumulation
Users can add positive habits they want to cultivate such as; exercising, reading, and, eating healthy. Each time they engage in a positive habit, they earn a point. Over time, these points accumulate. This will assist in reinforcing consistency and progress.

### 2. Negative Habit Awareness
Users can also log negative habits such as; excessive screen time, procrastination, and snacking on junk food. Each negative habit will subtract a point from their daily count to encourage self-reflection and behaviour change. 

### 3. Total Points 
This application allows you to clearly view you daily accumulated points at any time and see their progress. Users can decide what their daily or weekly goal is to allow them to celebrate milestones and foster a positive mindset.

### 4. Habit Reflection
Users can also review their habits that have already been added. This allows for users to understand whether they have prioritized fostering good habits or whether they have let their bad habits overtake their day. 

### 5. Habit Removal
Users can also remove a habit from the list. Maybe the user entered something incorrectly or the habit was something they didn't want to record.

## Implementation Plan 

### 1. Create The Menu, add the packages, create list.csv
Create the first python file.
Menu will have 6 possible options e.g:

    - add a good habit 
    - add a bad habit
    - check total points
    - view added habits
    - remove added habits
    - close the application

If option that was entered does not exist, print "please enter from options 1-6".

This will be done using the following code:  
```def create_menu():```
followed by each menu item.

The external packages implemented will be emoji and colored. This will allow for a stylised output rather for a more engaging output throughout the application.

Import codes & syntax:  

colored  
```from colored import Fore, Back, Style```  
example usage & syntax: ```print(f"{Fore.blue}Welcome to the good habits tracker application!{Style.reset}")```  

emoji  
```import emoji```  
example usage & syntax:
```print(emoji.emojize(f"{Back.blue}Thankyou for using the good habits tracker application!:thumbsup: {Style.reset}", language='alias'))```

Implement emoji & colored.


- Add habits list file, if file does not exist program it to create the file. Name list.csv.


### 3. Add Good Habits & Bad Habits function
- Create another python file to named application_functions.py.  
- Link the file.  
- Create good habits function.
- Create bad habits function.
- Make sure adds on a new line.
- Assign value for good habits (+1) and bad habits (-1).
- Add emoji.
- Add colored.

### 4. Check Total Points
- Create a function to check total points
- Make sure the function will add all the points together and print the sum.
- Add emoji 
- Add colored 
- Create a function to check whether the habit list exists for check points.
- Make sure it does not count first heading, only the points.

### 5. View Added Habits
- Create a function to print out list of added habits.
- Make sure it does not read first line headings.
- Make sure it does not print the points.
- Add emoji.
- Add colored.
- Create a function to check whether the habit list exists for view habits.

### 5. Remove a habit
- Create a function to delete the habit by checking table and appending table without the habit that the user has removed.
- Create a function to say that the habit has not been added yet to the list.
- Ensure it is functional with a new line not replacing headings in list.csv
- Implement emoji. 
- Add colored.












































































## Bibliography

Python Styling
- https://peps.python.org/pep-0008/

Colored Python Package
- https://pypi.org/project/colored/

Emoji Python Package
- https://pypi.org/project/emoji/
