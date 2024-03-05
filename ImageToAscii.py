#Loading the image in

from PIL import Image
im = Image.open(r'C:\Users\Luca\Pictures\cat.webp')
print(im.format, im.size, im.mode)
