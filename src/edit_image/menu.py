from src.edit_image.image_operations import *
import tkinter
from tkinter import filedialog  # SEPARATE IMPORT BECAUSE FILEDIALOG IS NOT IMPORTED WITH TKINTER


def edit_menu():
    """
    MENU FOR IMAGE EDITING,
    CONTAINS OPERATIONS THAT CAN BE PERFORMED ON AN EXISTING IMAGE
    """

    print("SELECTING FILE PATH...")
    window = tkinter.Tk()
    window.withdraw()  # HIDE TKINTER MAIN WINDOW
    file_path = filedialog.askopenfilename()  # OPEN FILE SELECT DIALOG
    print("SELECTED FILE PATH: ", file_path)



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
         6              go back to main menu''')

        edit_choice = input("ENTER CHOICE: ")

        if edit_choice == "1":
            adjust_brightness(file_path)
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
            print('\033[31m' + 'OPTION NOT FOUND' )
