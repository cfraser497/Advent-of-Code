from collections import deque, defaultdict

grid = []

with open("day20.txt", "r") as file:
    for line in file:
        grid.append(list(line.strip()))

def printgrid(g):
    for r in g:
        print("".join(list(map(str, r))))

def isInBounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

# up, right, down, left
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Find the start
ci, cj = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            ci, cj = i, j

# BFS To get distances
Q = deque([(ci, cj)])
dist = 0
path = []

while Q:
    ci, cj = Q.popleft()
    grid[ci][cj] = dist
    path.append((ci, cj))

    for di, dj in DIRS:
        ni, nj = ci + di, cj + dj

        if grid[ni][nj] == "." or grid[ni][nj] == "E":
            dist += 1
            Q.append((ni, nj))

# Loop over grid considering all possible cheats
over100 = 0
MAX_CHEAT_LENGTH = 2
cheats = defaultdict(int)

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if isinstance(grid[i][j], int):
            # We are on a path
            for di, dj in DIRS:
                walli, wallj = i + di, j + dj
                pathi, pathj = i + MAX_CHEAT_LENGTH * di, j + MAX_CHEAT_LENGTH * dj

                if isInBounds(walli, wallj) and isInBounds(pathi, pathj) and grid[walli][wallj] == "#" and isinstance(grid[pathi][pathj], int):
                    timesave = grid[pathi][pathj] - grid[i][j] - MAX_CHEAT_LENGTH

                    if timesave > 0:
                        cheats[timesave] += 1

                    if timesave >= 100:
                        over100 += 1 

print(over100)


# Part 2

over100 = 0
MAX_CHEAT_LENGTH = 20
MIN_TIMESAVE = 100
cheats = defaultdict(int)

# in my opinion, the questions is poorly worded T_T, unclear if a cheat can go in and out of walls
# Use a sliding window to determine possible cheats

for i, j in path:
    if grid[i][j] + MAX_CHEAT_LENGTH > dist:
        break
            
    if isinstance(grid[i][j], int):
        # We are on the path
        # Consider every grid point up to CHEAT_SIZE away from where we are
        for ei in range(i - MAX_CHEAT_LENGTH, i + MAX_CHEAT_LENGTH + 1):
            for ej in range(j - MAX_CHEAT_LENGTH, j + MAX_CHEAT_LENGTH + 1):
                cheatLength = abs(ei - i) + abs(ej - j)
                if isInBounds(ei, ej) and cheatLength <= MAX_CHEAT_LENGTH and isinstance(grid[ei][ej], int):
                    # We can make it here by a cheat
                    timesave = grid[ei][ej] - grid[i][j] - cheatLength

                    if timesave >= MIN_TIMESAVE:
                        over100 += 1
                        cheats[timesave] += 1


# print(sorted(cheats.items(), reverse=True))
print(over100)