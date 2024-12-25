# Inspiration for this logic has been taken from open source code and other solutions

from sys import argv
from heapq import heappop, heappush
from math import inf

with open('Day16\data.txt','r') as f:
    lines = [l.strip() for l in f]

dimx, dimy = (len(lines[0]), len(lines))
maze = list("".join(lines))
start, end = (maze.index("S"), maze.index("E"))
dirs = [-dimx, 1, dimx, -1]

visited = dict()
q = list()
highscore = inf
paths = list()

heappush(q, (0, start, 1, ""))
while q:
    score, pos, d, path = heappop(q)
    if score > highscore:
        break
    if (pos, d) in visited and visited[(pos, d)] < score:
        continue
    visited[(pos, d)] = score
    if pos == end:
        highscore = score
        paths.append(path)
    if maze[pos+dirs[d]] != "#":
        heappush(q, (score+1, pos+dirs[d], d, path+"F"))
    heappush(q, (score+1000, pos, (d+1)%4, path+"R"))
    heappush(q, (score+1000, pos, (d-1)%4, path+"L"))

tiles = set()
tiles.add(start)
for p in paths:
    t, d = (start, 1)
    for c in p:
        if c=="L": d=(d-1)%4
        elif c=="R": d=(d+1)%4
        elif c=="F":
            t+=dirs[d]
            tiles.add(t)
print(f"Shortest path: {highscore}")
print(f"Optimal viewing positions: {len(tiles)}")