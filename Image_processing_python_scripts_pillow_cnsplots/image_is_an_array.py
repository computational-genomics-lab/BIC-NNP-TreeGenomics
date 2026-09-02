from PIL import Image

import numpy as np
img = Image.open("3.tif")

arr = np.array(img)

print(arr.shape)
print(arr.dtype)
