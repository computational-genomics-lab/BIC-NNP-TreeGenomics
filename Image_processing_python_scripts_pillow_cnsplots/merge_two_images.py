from PIL import Image

img1 = Image.open("3.tif")

img2 = Image.open("5.tif")

h = min(img1.height, img2.height)

merged = Image.new("RGB", (img1.width + img2.width, h))

merged.paste(img1, (0, 0))
merged.paste(img2, (img1.width, 0))

print("img1:", img1.size)
print("img2:", img2.size)
print("merged:", merged.size)
merged.save("merged.png")
merged.show()
