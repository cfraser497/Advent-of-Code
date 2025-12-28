from collections import deque

with open("day16.txt", "r") as file:
    grid = file.read().strip().split("\n")

def printgrid(g):
    for r in g:
        print("".join(r))


grid = [list(r) for r in grid]

## Find start and end
si, sj, ei, ej = 0, 0, 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            si, sj = i, j
        if grid[i][j] == "E":
            ei, ej = i, j

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 0: up 1: east 2: south 3: west
sDir = 1

Q = deque([(si, sj, sDir)])

# Maps keys (i, j, dir) -> minWeight
tileScores = {(si, sj, sDir): 0}

while Q:
    ci, cj, cDir = Q.popleft()

    for didx, (di, dj) in enumerate(DIRS):
        ni, nj = ci + di, cj + dj

        if grid[ni][nj] == "." or grid[ni][nj] == "E":
            if (ni, nj, didx) not in tileScores:
                tileScores[(ni, nj, didx)] = tileScores[(ci, cj, cDir)] + (1 if didx == cDir else 1001)
                Q.append((ni, nj, didx))
        
            else:
                # We have been here before
                newWeight = tileScores[(ci, cj, cDir)] + (1 if didx == cDir else 1001)

                if newWeight < tileScores[(ni, nj, didx)]:
                    tileScores[(ni, nj, didx)] = newWeight
                    Q.append((ni, nj, didx))
    
scores = []
for di in range(len(DIRS)):
    if (ei, ej, di) in tileScores:
        scores.append(tileScores[ei, ej, di])

score = min(scores)
print(score)


## Part 2

Q = deque([(ei, ej, score)])
bestTiles = set({(ei, ej)})

while Q:
    ci, cj, csc = Q.popleft()

    for di, dj in DIRS:
        ni, nj = ci + di, cj + dj

        for didx in range(len(DIRS)):
            if (ni, nj, didx) in tileScores:
                if tileScores[(ni, nj, didx)] == csc - 1:
                    Q.append((ni, nj, csc - 1))
                    bestTiles.add((ni, nj))
                elif tileScores[(ni, nj, didx)] == csc - 1001:
                    Q.append((ni, nj, csc - 1001))
                    bestTiles.add((ni, nj))

for i, j in bestTiles:
    grid[i][j] = "O"

printgrid(grid)
print(len(bestTiles))