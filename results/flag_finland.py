from PIL import Image
import numpy as np

a = np.zeros((300, 500, 3), dtype=np.uint8)
# unsigned 8-bit integer (1 byte)

a[:, :, :] = 255
a[110:190, :, :2] = 0
a[:, 150:230, :2] = 0

im = Image.fromarray(a)
im.save('finland.png')
