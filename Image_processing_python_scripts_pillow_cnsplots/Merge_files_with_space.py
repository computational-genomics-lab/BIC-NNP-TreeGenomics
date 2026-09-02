from PIL import Image

img1 = Image.open("3.tif")
img2 = Image.open("5.tif")

# Convert to RGB
img1 = img1.convert("RGB")
img2 = img2.convert("RGB")

# Space between images
gap = 20

# Use the smaller height
h = min(img1.height, img2.height)

# Create canvas with extra space
merged = Image.new(
    "RGB",
    (img1.width + gap + img2.width, h),
    "white"
)

# Paste image 1
merged.paste(img1, (0, 0))

# Paste image 2 after the gap
merged.paste(img2, (img1.width + gap, 0))

print("img1:", img1.size)
print("img2:", img2.size)
print("merged:", merged.size)

merged.save("merged_with_gap.png")
merged.show()