from PIL import Image, ImageDraw
from random import randint

def draw_bit(x, y, bit):
  a = pix[(x,y)]
  draw.point((x,y),(int(bin(a[0])[:-1] + bit,2),a[1],a[2]))

def str_to_bit(s):
  return "".join(f"{ord(i):08b}" for i in s)

#print("Image:")
#im_name = input()
print("Message:")
message = input()
message = str_to_bit(message)

image = Image.open("Lenna.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

#Key generation
key = []
[key.append([randint(0, height - 1),randint(0, width - 1)]) for i in range(len(message))]
with open("key.txt", "w") as f:
  for i in range(len(key)):
    f.write(str(key[i][0]) + " " + str(key[i][1]) + "\n")

i = 0
for j in key:
  draw_bit(j[0],j[1],message[i])
  i += 1

image.save("Lenna+msg.png", "PNG")+
del draw