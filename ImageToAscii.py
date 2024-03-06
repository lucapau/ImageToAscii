
from PIL import Image

#Loading the image in

im = Image.open(r'C:\Users\Luca\Pictures\cat.webp')
print(im.format, im.size, im.mode)

# resizing and grayscalling

newsize = (1000, 1000)
im = im.resize(newsize)
# grayscale
im = im.convert('L') 
im.show()

