from PIL import Image, ImageFilter

img = Image.open("3.tif")

edges = img.filter(ImageFilter.FIND_EDGES)
edges.save("edges.jpg")

edges.show()
