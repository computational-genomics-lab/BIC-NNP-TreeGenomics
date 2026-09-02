
from PIL import Image, ImageEnhance
img = Image.open("3.tif")
gray = img.convert("L")
gray.save("gray.jpg")
bright = ImageEnhance.Brightness(img).enhance(1.5)
bright.save("bright.jpg")
contrast = ImageEnhance.Contrast(img).enhance(1.5)
contrast.save("contrast.jpg")

gray.show()
bright.show()
contrast.show()
