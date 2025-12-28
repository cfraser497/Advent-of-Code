grid = []
ans = 0

with open("day4.txt", "r") as file:
    for line in file:
        grid.append(line.strip())

n = len(grid)

# Search horizontally

target = "XMAS"

for line in grid:
    for i in range(n - len(target) + 1):
        section = line[i: i + len(target)]
        if section == target or section == target[::-1]:
            ans += 1


print(ans)

# Search vertically

for i in range(n - len(target) + 1):
    for j in range(n):
        section = "".join([row[j] for row in grid[i: i + len(target)]])
        if section == target or section == target[::-1]:
            ans += 1

print(ans)

# Search diagonally right 

for i in range(n - len(target) + 1):
    for j in range(n - len(target) + 1):
        section = "".join(row[j + k] for k, row in enumerate(grid[i: i + len(target)]))
        if section == target or section == target[::-1]:
            ans += 1

print(ans)

# Search diagonally left

for i in range(n - len(target) + 1):
    for j in range(len(target) - 1, n):
        section = "".join(row[j - k] for k, row in enumerate(grid[i: i + len(target)]))
        if section == target or section == target[::-1]:
            ans += 1

print(ans)

## PART 2

ans = 0
target = "MAS"

# Search diagonally right 

for i in range(n - len(target) + 1):
    for j in range(n - len(target) + 1):
        section = "".join(row[j + k] for k, row in enumerate(grid[i: i + len(target)]))
        if section == target or section == target[::-1]:
            if grid[i + 2][j] == 'S' and grid[i][j + 2] == 'M' or grid[i + 2][j] == 'M' and grid[i][j + 2] == 'S':
                ans += 1

print(ans)