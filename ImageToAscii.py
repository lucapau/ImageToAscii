from PIL import Image

# Loading the image
im = Image.open(r'C:\Users\Luca\Pictures\cat.webp')

# Resizing
new_width = 200
ratio = im.height / im.width
new_height = int(new_width * ratio * 0.5)
im = im.resize((new_width, new_height))

# Grayscaling
im = im.convert('L')
WIDTH, HEIGHT = im.size

# Mapping grayscale pixels to ASCII characters
data = list(im.getdata())
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

ascii_chars = "@$%#*+=-:. "

# Scaling factor for ASCII characters
scale = (len(ascii_chars)-1) / 255.0

# Generating ASCII art
with open("output.txt", "w") as file:
    for row in data:
        file.write("".join(ascii_chars[int(value * scale)] for value in row) + "\n")
