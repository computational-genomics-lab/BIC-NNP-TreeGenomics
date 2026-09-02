from PIL import Image

img = Image.open("3.tif")

cropped = img.crop((100, 60, 700, 400))
cropped.save("cropped.jpg")
rotated = img.rotate(90, expand=True)

rotated.save("rotated.jpg")

flipped = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

flipped.save("flipped.jpg")

cropped.show()
rotated.show()
flipped.show()
