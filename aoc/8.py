from collections import Counter
import sys

for line in sys.stdin:
    data = line

size = 25*6

layers = []
for i in range(len(data)//size):
    layers.append(data[i*size:(i+1)*size])
print(len(layers))

ldata = [(x,Counter(x)) for x in layers]
zerolayer = min(ldata, key=lambda x: x[1]['0'])
print(zerolayer)
print(zerolayer[1]['1']*zerolayer[1]['2'])
print(zerolayer[1]['1'], zerolayer[1]['2'])