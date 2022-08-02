import os

from PIL import Image, ImageEnchance, ImageFilter

path = " ./imgs"
pathOut = " ./editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #sharpening , BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    #contrast ,
    factor = 1.5
    enhancer = ImageEnchance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f';{pathOut}/{clean_name}_edited.jpg')

