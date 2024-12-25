# Inspiration for this logic has been taken from open source code and other solutions

from re import findall
data = open("Day14\data.txt").read()
W, H = 101, 103

robots = [[int(n) for n in findall(r"(-?\d+)", item)] for item in data.split("\n")]

def simulate(t):
    return [((sx + t*vx) % W, (sy + t*vy) % H) for (sx, sy, vx, vy) in robots]

from statistics import variance
bx, bxvar, by, byvar = 0, 10*100, 0, 10*1000
for t in range(max(W,H)):
    xs, ys = zip(*simulate(t))
    if (xvar := variance(xs)) < bxvar: bx, bxvar = t, xvar
    if (yvar := variance(ys)) < byvar: by, byvar = t, yvar
print("Part 2:", bx+((pow(W, -1, H)*(by-bx)) % H)*W)
