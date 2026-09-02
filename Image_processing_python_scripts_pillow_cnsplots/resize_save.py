from PIL import Image

img = Image.open("3.tif")

resized = img.resize((400, 300))
resized.save("resized.jpg")

print("Original:", img.size)

print("Resized:", resized.size)

resized.show()

