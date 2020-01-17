from collections import Counter
import sys

for line in sys.stdin:
    data = line

size = 25*6

layers = []
for i in range(len(data)//size):
    layers.append(data[i*size:(i+1)*size])

pdata = []
for pixel in range(len(layers[0])):
    for l in layers:
        if l[pixel] == '0':
            pdata.append(0)
            break
        elif l[pixel] == '1':
            pdata.append(1)
            break

cval = 0
for i in range(6):
    for j in range(25):
        print('▣' if pdata[25*i+j] == 1 else ' ',end=' ')
    print()
