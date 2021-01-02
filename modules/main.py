from PIL import Image, ImageFilter
from copy import deepcopy

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
# help(img)

img = Image.open("./pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.SHARPEN)
converted_img = img.convert("L")
rotated_img = converted_img.rotate(57)
resized_img = converted_img.resize((300, 300))

box = (100, 100, 400, 400)
region = img.crop(box)
region.save("./edited_imgs/cropped.png", "PNG")

astro_img = Image.open("./unsplash/astro.jpg")
small_astro_thumbnail = deepcopy(astro_img).thumbnail((400, 200))
# if using resize the image might be squished, use thumbnail method to retain aspect ratio
small_astro_img = astro_img.resize((400, 200))

# png format supports image filters
filtered_img.save("./edited_imgs/shar.png", "PNG")
# filtered_img.show()
converted_img.save("./edited_imgs/grey.png", "PNG")
resized_img.save("./edited_imgs/resized.png", "PNG")
rotated_img.save("./edited_imgs/rotated.png", "PNG")
# converted_img.show()

astro_img.save("./edited_imgs/another_astro.jpg", "JPEG")
small_astro_img.save("./edited_imgs/small_astro.jpg", "JPEG")
small_astro_thumbnail.save("./edited_imgs/thumbnail_astro.jpg", "JPEG")
