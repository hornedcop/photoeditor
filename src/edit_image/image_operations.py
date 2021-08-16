from PIL import Image
from PIL import ImageFilter
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
    img = Image.open(file_path)  # CREATES AN IMAGE OBJECT
    edited_img = Enhance.Contrast(img)  # CREATES AN IMAGE OBJECT WHOSE CONTRAST CAN BE CHANGED

    print("HINT: 0 AS CONTRAST FACTOR GIVES A GREY IMAGE",
          "      1 AS CONTRAST FACTOR GIVES ORIGINAL IMAGE",
          "      NEGATIVE VALUES INVERT THE IMAGE", sep="\n")

    while True:
        try:
            factor = float(input('Enter the Contrast factor : '))
            break
        except ValueError:
            print('\033[31m' + 'INVALID INPUT' + '\033[0m')

    edited_img = edited_img.enhance(factor)

    if input("do you want to see this image (y/n): ").lower() == "y":
        edited_img.show()
    if input("do you want to save this image (y/n): ").lower() == "y":
        new_file = auto_renamed_writable_file(file_path)
        edited_img.save(new_file)
        new_file.close()


def add_filters(file_path):
    print("THE FOLLOWING FILTERS ARE AVAILABLE ⬇️",
          "1: BLUR",
          "2: CONTOUR",
          "3: DETAIL",
          "4: EDGE ENHANCE",
          "5: HIGH EDGE ENHANCE",
          "6: EMBOSS",
          "7: FIND EDGES",
          "8: SHARPEN",
          "9: SMOOTH",
          "10: HIGH SMOOTH", sep="\n")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if not (0 < choice < 6):
                raise ValueError
            break
        except ValueError:
            print('\033[31m' + 'INVALID INPUT' + '\033[0m')

    choice_map = {
        1: ImageFilter.BLUR,
        2: ImageFilter.CONTOUR,
        3: ImageFilter.DETAIL,
        4: ImageFilter.EDGE_ENHANCE,
        5: ImageFilter.EDGE_ENHANCE_MORE,
        6: ImageFilter.EMBOSS,
        7: ImageFilter.FIND_EDGES,
        8: ImageFilter.SHARPEN,
        9: ImageFilter.SMOOTH,
        10: ImageFilter.SMOOTH_MORE,
    }

    img = Image.open(file_path)
    edited_img = img.filter(choice_map[choice])

    if input("do you want to see this image (y/n): ").lower() == "y":
        edited_img.show()
    if input("do you want to save this image (y/n): ").lower() == "y":
        new_file = auto_renamed_writable_file(file_path)
        edited_img.save(new_file)
        new_file.close()


def resize_img(file_path):
    return


def crop_img(file_path):
    return
