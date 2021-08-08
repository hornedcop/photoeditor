from PIL import Image
from random import randrange


def generate_random_pixels():
    # GET IMAGE SIZE
    while True:
        try:
            width, height = int(input("ENTER IMAGE WIDTH: ")), int(input("ENTER IMAGE HEIGHT: "))
            break
        except ValueError:
            print("INVALID INPUT, TRY AGAIN...")

    print("GENERATING RANDOM PIXELS...")

    pixel_list = []  # INITIALIZE PIXEL LIST
    for x in range(width):  # PUT RANDOM COLOR VALUES FOR EACH PIXEL
        for y in range(height):
            # THREE VALUED TUPLE CONTAINING RANDOM RED, GREEN, BLUE VALUES BETWEEN 0 AND 255 (INCLUSIVE)
            pixel_list.append((
                # PIXEL COLOR VALUES
                randrange(0, 256),  # RED
                randrange(0, 256),  # GREEN
                randrange(0, 256)  # BLUE
            ))

    print("DONE GENERATING RANDOM PIXELS!")
    return pixel_list, width, height


def save_rand_img():
    pixel_list, width, height = generate_random_pixels()

    # PILLOW IMAGE OBJECT
    img = Image.new(mode="RGB", size=(width, height))
    img.putdata(pixel_list)  # SET NEW IMAGE'S PIXEL DATA TO RANDOMLY GENERATED PIXEL LIST

    if input("Do you wish to see image before saving? (y/n): ").lower() == "y":
        img.show()
        if input("Do you still wish to save this image? (y/n): ").lower() == "y":
            file_name = input("Enter file name to save: ") + ".png"
            img.save(file_name)
    else:
        file_name = input("Enter file name to save: ") + ".png"
        img.save(file_name)


def display_rand_img():
    pixel_list, width, height = generate_random_pixels()

    # PILLOW IMAGE OBJECT
    img = Image.new(mode="RGB", size=(width, height))
    img.putdata(pixel_list)  # SET NEW IMAGE'S PIXEL DATA TO RANDOMLY GENERATED PIXEL LIST
    img.show()
