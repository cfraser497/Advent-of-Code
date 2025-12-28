from collections import deque

bs = []
with open("day18.txt", "r") as file:
    for line in file:
        x, y = line.strip().split(",")
        bs.append((int(x), int(y)))

def printgrid(g):
    for r in g:
        print("".join(r))


MAX_X = 70
MAX_Y = 70
BYTE_NUM = 1024
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

grid = [["." for _ in range(MAX_X + 1)] for _ in range(MAX_Y + 1)]

# Fill in the grid
for i in range(BYTE_NUM):
    x, y = bs[i]
    grid[y][x] = "#"


# BFS
def findPath(grid):
    Q = deque([(0, 0, 0)])
    visited = set({(0, 0)})

    while Q:
        i, j, d = Q.popleft()
        if i == MAX_Y and j == MAX_X:
            return d

        for di, dj in DIRS:
            ni, nj = i + di, j + dj

            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and grid[ni][nj] != "#":
                visited.add((ni, nj))
                Q.append((ni, nj, d + 1))

    return None

print(findPath(grid))

# Part 2

for i in range(BYTE_NUM, len(bs)):
    x, y = bs[i]
    grid[y][x] = "#"

    if findPath(grid) == None:
        print(f"{x}, {y}")
        break
