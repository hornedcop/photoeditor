from PIL import Image
from PIL import ImageEnhance as ie


def adjust_brightness(file_path):
    img = Image.open(file_path)
    edited_img = ie.Brightness()
    while True:
        try:
            factor = float(input('Enter the Brightness factor : '))
            break
        except ValueError:
            print('\033[31m' + 'INVALID INPUT' + '\033[0m')
    if factor != 0 :
        edited_img = edited_img.enhance(factor)
        edited_img.show()



    else :
        print("no changes done")
        img.show()









def change_contrast(file_path):
    return


def add_filters(file_path):
    return


def resize_img(file_path):
    return


def crop_img(file_path):
    return
