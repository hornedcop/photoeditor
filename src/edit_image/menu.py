import tkinter
from tkinter import filedialog


window = tkinter.Tk()
window.withdraw()
file_path = filedialog.askopenfilename()


def edit_menu():
    while True:
        print('''
    ╔═╦═╦═╦══╦══╗        ╔══╦═╦═╗
    ║╬║╬║╦╣══╣══╣        ║═╦╣║║╬║
    ║╔╣╗╣╩╬══╠══║        ║╔╝║║║╗╣
    ╚╝╚╩╩═╩══╩══╝        ╚╝─╚═╩╩╝

         1              adjust brightness
         2              change contrast
         3              adding filters
         4              resizing the image
         5              crop the image
         6              go back to main menu ''')

        edit_choice = input("ENTER CHOICE: ")
        print("CHOOSE FILE PATH: ")

        if edit_choice == "1":
            adjust_birghtness(file_path)
        elif edit_choice == "2":
            change_contrast(file_path)
        elif edit_choice == "3":
            add_filters(file_path)
        elif edit_choice == "4":
            resize_img(file_path)
        elif edit_choice == "5":
            crop_img(file_path)
        elif edit_choice == "6":
            break
        else:
            print('\033[31m' + 'OPTION NOT FOUND' + '\033[0m')


edit_menu()
