
from PIL import Image

#Loading the image in

im = Image.open(r'C:\Users\Luca\Pictures\monalisa.jpg')
print(im.format, im.size, im.mode)

# resizing and grayscalling

newsize = (100, 100)
im = im.resize(newsize)
# grayscale
im = im.convert('L') 
WIDTH, HEIGHT = im.size


#assigning ascii characters to graysclae pixel values

data = list(im.getdata()) 

data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

ascii_chars = "@$%#*+=-:."
scale = (len(ascii_chars)-1)/255.
print()
for row in data:
    print(''.join(ascii_chars[int(value*scale)] for value in row))
