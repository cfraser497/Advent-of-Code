grid = []

with open("day12.txt", "r") as file:
    grid = file.read().strip().split('\n')

visited = set()
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def isInBounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def dfs(i, j):
    totalA, totalP, totalC = 1, 0, 0

    for didx, (di, dj) in enumerate(directions):
        ni, nj = i + di, j + dj
        di90, dj90 = directions[(didx + 1) % len(directions)]
        ni90, nj90 = i + di90, j + dj90

        # Calculate interior corners
        if isInBounds(ni, nj) and isInBounds(ni90, nj90)\
              and grid[ni][nj] != grid[i][j] and grid[ni90][nj90] != grid[i][j]:
            # We have this (or rotation): 
            # B B B
            # B + -
            # B | A
            totalC += 1
        
        # Calcuate corners on the border
        if (isInBounds(ni, nj) and not isInBounds(ni90, nj90) and grid[ni][nj] != grid[i][j]) or\
            (not isInBounds(ni, nj) and isInBounds(ni90, nj90) and grid[ni90][nj90] != grid[i][j]):
            # We have this (or rotation):
            # A
            # -
            # B
            totalC += 1

        # This only works for square grids
        if not isInBounds(ni, nj) and not isInBounds(ni90, nj90):
            # We are at the corner of the grid
            totalC += 1

        # Calculate exterior corners
        di45, dj45 = i + di + di90, j + dj + dj90
        if isInBounds(ni, nj) and isInBounds(ni90, nj90) and grid[ni][nj] == grid[i][j]\
              and grid[ni90][nj90] == grid[i][j] and grid[di45][dj45] != grid[i][j]:
            # We have this (or rotation):
            # A | B
            # A + -
            # A A A
            totalC += 1

        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == grid[i][j]:
            if (ni, nj) not in visited: 
                visited.add((ni, nj))
                a, p, c = dfs(ni, nj)
                totalA += a
                totalP += p
                totalC += c
        else:
            totalP += 1

    return (totalA, totalP, totalC)

regions = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in visited:
            visited.add((i, j))
            regions.append(dfs(i, j))

print(regions)
totalp1 = 0
totalp2 = 0
for a, p, c in regions:
    totalp1 += a * p
    totalp2 += a * c

print(totalp1)
print(totalp2)