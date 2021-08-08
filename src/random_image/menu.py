from src.random_image.generate_img import *


def random_menu():
    while True:
        print('''
         _____ _____ _____ _____ _____                        _____ _____ _____ 
        |  _  | __  |   __|   __|   __|                      |   __|     | __  |
        |   __|    -|   __|__   |__   |                      |   __|  |  |    -|
        |__|  |__|__|_____|_____|_____|                      |__|  |_____|__|__|

                1                                               CREATE RANDOM IMAGE AND SAVE IT
                2                                               DISPLAY RANDOM IMAGE
                3                                               RETURN TO MAIN MENU...''')

        choice = input("ENTER CHOICE: ")
        if choice == "1":
            save_rand_img()
        elif choice == "2":
            display_rand_img()
        elif choice == "3":
            return
        else:
            print("INVALID CHOICE, TRY AGAIN...")
