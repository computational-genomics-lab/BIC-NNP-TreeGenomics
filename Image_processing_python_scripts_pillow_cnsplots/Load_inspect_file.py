from PIL import Image
img = Image.open("3.tif")

print("Format:", img.format)

print("Mode:", img.mode)

print("Size:", img.size)
img.show()

