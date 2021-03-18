from PIL import Image

image = Image.open("Lenna+msg.png")
pix = image.load()
with open("key.txt") as f:
    key = []
    for line in f:
        key.append([int(i) for i in line.split()])

result = "".join(bin(pix[j[0], j[1]][0])[-1] for j in key)
s = "".join(chr(int(result[8 * i:(i + 1) * 8], 2)) for i in range(len(result) // 8))
print(s)
image.close()
