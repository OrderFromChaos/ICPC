class V:
    def __init__(self, pos, edges):
        self.pos = pos # (x,y)
        self.edges = edges # [(x,y),(x,y),...]
    def __repr__(self):
        return str((self.pos,self.edges))

ydim = int(input())
xdim = int(input())

# Create graph
vertices = dict()
for y in range(ydim):
    walls = [str(bin(int(w)))[2:].rjust(4,'0') for w in input().split()] # rjust pads zeroes until 4 length
#    print(walls)
    for x, val in enumerate(walls):
        edges = []

        # Have to read bytes backwards (2^0 is last digit)
        if val[-1] == '0': # West
            maybe = (x-1,y)
            if 0 <= maybe[0] <= xdim-1 and 0 <= maybe[1] <= ydim-1:
                edges.append(maybe)

        if val[-2] == '0': # North
            maybe = (x,y-1)
            if 0 <= maybe[0] <= xdim-1 and 0 <= maybe[1] <= ydim-1:
                edges.append(maybe)

        if val[-3] == '0': # East
            maybe = (x+1,y)
            if 0 <= maybe[0] <= xdim-1 and 0 <= maybe[1] <= ydim-1:
                edges.append(maybe)

        if val[-4] == '0': # South
            maybe = (x,y+1)
            if 0 <= maybe[0] <= xdim-1 and 0 <= maybe[1] <= ydim-1:
                edges.append(maybe)

        vertices[(x,y)] = V((x,y),edges) # Somewhat redundant, but makes later code easier


# for i in vertices:
#     print(i,vertices[i])

# Find all rooms
rooms = [] # sizes
seen = set() # found already as part of a room
for pos in vertices:
    if pos not in seen:
        seen.add(pos)
        room_size = 1

#        print('New room!')
        tosearch = vertices[pos].edges
        while tosearch: # Non-empty
#            print(tosearch)
            checking = vertices[tosearch.pop()] # Removes last item of list and returns it
            seen.add(checking.pos)
            room_size += 1
            tosearch += [x for x in checking.edges if x not in seen]
        rooms.append(room_size)
#        print(room_size)

print(len(rooms))
print(max(rooms))
