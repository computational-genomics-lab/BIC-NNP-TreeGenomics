from PIL import Image, ImageFilter
img = Image.open("3.tif")
blurred = img.filter(
    ImageFilter.GaussianBlur(radius=3)
)
blurred.save("blurred.jpg")

sharpened = img.filter(ImageFilter.SHARPEN)
sharpened.save("sharpened.jpg")

blurred.show()
sharpened.show()
