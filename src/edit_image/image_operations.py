from PIL import Image
from PIL import ImageEnhance as Enhance
from src.edit_image._helpers import *


def adjust_brightness(file_path):
    img = Image.open(file_path)  # CREATES AN IMAGE OBJECT
    edited_img = Enhance.Brightness(img)  # CREATES AN IMAGE OBJECT WHOSE BRIGHTNESS CAN BE CHANGED

    # HINT FOR THE USER, AS ONE COULD THINK 0 MEANS NO CHANGE.
    print("HINT: 0 AS BRIGHTNESS FACTOR GIVES A BLACK IMAGE",
          "      1 AS BRIGHTNESS FACTOR GIVES ORIGINAL IMAGE", sep="\n")

    while True:
        try:
            factor = float(input('Enter the Brightness factor : '))
            break
        except ValueError:
            print('\033[31m' + 'INVALID INPUT' + '\033[0m')

    edited_img = edited_img.enhance(factor)

    if input("Do you want to see this image (y/n): ").lower() == "y":
        edited_img.show()
    if input("Do you want to save this image (y/n): ").lower() == "y":
        new_file = auto_renamed_writable_file(file_path)
        edited_img.save(new_file)
        new_file.close()


def change_contrast(file_path):
    return


def add_filters(file_path):
    return


def resize_img(file_path):
    return


def crop_img(file_path):
    return
