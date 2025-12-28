from collections import defaultdict

grid = []

with open("ex.txt", "r") as file:
    grid = file.read().split()

# Maps frequencies -> [(x, y)]
antennas = defaultdict(list)

for i in range(len(grid)):
    grid[i] = grid[i].strip()
    for j in range(len(grid[0])):
        c = grid[i][j]

        if c != ".":
            antennas[c].append((i, j))

antinodes = set()
antinodesp2 = set()

for freq, locs in antennas.items():
    if len(locs) < 2:
        continue
    
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            yi, xi = locs[i]
            yj, xj = locs[j]

            distx, disty = xj - xi, yj - yi

            n1x, n1y = xi - distx, yi - disty
            n2x, n2y = xj + distx, yj + disty

            if 0 <= n1y < len(grid) and 0 <= n1x < len(grid[0]):
                antinodes.add((n1y, n1x))
            if 0 <= n2y < len(grid) and 0 <= n2x < len(grid[0]):
                antinodes.add((n2y, n2x))


            antinodesp2.add((yi, xi))
            antinodesp2.add((yj, xj))

            while 0 <= n1y < len(grid) and 0 <= n1x < len(grid[0]):
                antinodesp2.add((n1y, n1x))
                n1y -= disty
                n1x -= distx

            while 0 <= n2y < len(grid) and 0 <= n2x < len(grid[0]):
                antinodesp2.add((n2y, n2x))
                n2y += disty
                n2x += distx
            

print(len(antinodes))
print(len(antinodesp2))
