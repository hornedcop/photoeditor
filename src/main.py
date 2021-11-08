import os
import sys
path = os.getcwd()
if path.endswith("src"):
    path = path[:-3]
sys.path.append(path)

# ACTUAL CODE BEGINS HERE
from edit_image.menu import edit_menu
from random_image.menu import random_menu
from datetime import datetime
from backend import get_db

user_data = get_db()
username = user_data["name"]
dob = user_data["dob"]

today = datetime.today()
is_birthday = [int(today.day), int(today.month)] == dob[:-1]


def menu():
    # Greeting
    print("\033[44m" + f"GOOD MORNING, {username}" + "\033[0m")
    if is_birthday:
        print("Happy birthday to you!!!")
    print("Let's start editing!")

    while True:
        print('''
 _____ _____ _____ _____ _____                        _____ _____ _____ 
|  _  | __  |   __|   __|   __|                      |   __|     | __  |
|   __|    -|   __|__   |__   |                      |   __|  |  |    -|
|__|  |__|__|_____|_____|_____|                      |__|  |_____|__|__|

        1                                               Edit a photo
        2                                               Generate a random image
        3                                               EXIT''')

        choice = input("Enter your choice : ")
        if choice == "1":
            edit_menu()
        elif choice == "2":
            random_menu()
        elif choice == "3":
            print('Sayōnara')
            break
        else:
            print('\033[31m' + 'OPTION NOT FOUND' + '\033[0m')


menu()
