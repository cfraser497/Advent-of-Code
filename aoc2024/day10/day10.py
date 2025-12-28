grid = []

with open("ex.txt", "r") as file:
    grid = file.read().strip().split()

for i in range(len(grid)):
    grid[i] = [int(x) for x in grid[i]]

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
visited = set()

def dfs(i, j, nextH) -> int:
    # For part 2, simply comment out the visited adding component of the problem
    visited.add((i, j))
    if nextH == 10:
        return 1
    score = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj

        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited and grid[ni][nj] == nextH:
            score += dfs(ni, nj, nextH + 1)
    
    return score


totalScore = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            visited = set()
            totalScore += dfs(i, j, 1)

# print(grid)
print(totalScore)