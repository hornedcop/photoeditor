from PIL import Image
from random import randrange


def generate(width, height):
    img_data = []  # INITIALIZE IMAGE DATA LIST
    # PUT RANDOM COLOR VALUES FOR EACH PIXEL
    for x in range(width):
        for y in range(height):
            img_data.append((
                # PIXEL COLOR VALUES
                randrange(0, 256),  # RED
                randrange(0, 256),  # GREEN
                randrange(0, 256)  # BLUE
            ))

    # PILLOW IMAGE OBJECT
    img = Image.new(mode="RGB", size=(width, height))
    img.putdata(img_data)  # SET NEW IMAGE'S PIXEL DATA TO RANDOM GENERATED PIXELS

    return img
