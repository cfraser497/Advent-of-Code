grid = []
instructions = []

def printgrid(grid):
    for r in grid:
        print("".join(r))
    print("\n")

with open("exbig.txt", "r") as file:
    g, instructions = file.read().strip().split("\n\n")

    grid = g.split("\n")
    grid = [list(r) for r in grid]

# PART 2
gridcopy = [row[:] for row in grid]


# Find the robot
ri, rj = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            ri, rj = i, j

print(instructions)
# Run the simulation
for d in instructions:
    pushi, pushj = ri, rj
    if d == "^":
        pushi -= 1
        while pushi >= 0 and grid[pushi][rj] == "O":
            pushi -= 1

        if grid[pushi][rj] == ".":
            # There is space to push
            for i in range(pushi, ri):
                grid[i][rj] = grid[i + 1][rj]
            grid[ri][rj] = "."
            ri -= 1

    elif d == ">":
        pushj += 1
        while pushj < len(grid[0]) and grid[ri][pushj] == "O":
            pushj += 1
        
        if grid[ri][pushj] == ".":
            # There is space to push
            for j in range(pushj, rj, -1):
                grid[ri][j] = grid[ri][j - 1]
            grid[ri][rj] = "."
            rj += 1

    elif d == "<":
        pushj -= 1
        while pushj >= 0 and grid[ri][pushj] == "O":
            pushj -= 1
        
        if grid[ri][pushj] == ".":
            # There is space to push
            for j in range(pushj, rj):
                grid[ri][j] = grid[ri][j + 1]
            grid[ri][rj] = "."
            rj -= 1

    elif d == "v":
        pushi += 1
        while pushi < len(grid) and grid[pushi][rj] == "O":
            pushi += 1
        
        if grid[pushi][rj] == ".":
            # There is space to push
            for i in range(pushi, ri, -1):
                grid[i][rj] = grid[i - 1][rj]
            grid[ri][rj] = "."
            ri += 1

    # printgrid(grid)

# Calculate boxes
total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            total += 100 * i + j

# printgrid(grid)
# print(total)


## PART 2

widegrid = []
grid = gridcopy
for i in range(len(grid)):
    row = []
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            row.extend([".", "."])
        elif grid[i][j] == "O":
            row.extend(["[", "]"])
        elif grid[i][j] == "#":
            row.extend(["#", "#"])
        elif grid[i][j] == "@":
            row.extend(["@", "."])
    widegrid.append(row)

grid = widegrid
printgrid(grid)

# Find the robot
ri, rj = 0, 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            ri, rj = i, j


# Run the simulation
for d in instructions:
    pushi, pushj = ri, rj
    if d == "^":
        pushi -= 1
        while pushi >= 0 and grid[pushi][rj] == "O":
            pushi -= 1

        if grid[pushi][rj] == ".":
            # There is space to push
            for i in range(pushi, ri):
                grid[i][rj] = grid[i + 1][rj]
            grid[ri][rj] = "."
            ri -= 1

    elif d == ">":
        pushj += 1
        while pushj < len(grid[0]) and (grid[ri][pushj] == "[" or grid[ri][pushj] == "]"):
            pushj += 1
        
        if grid[ri][pushj] == ".":
            # There is space to push
            for j in range(pushj, rj, -1):
                grid[ri][j] = grid[ri][j - 1]
            grid[ri][rj] = "."
            rj += 1

    elif d == "<":
        pushj -= 1
        while pushj >= 0 and (grid[ri][pushj] == "[" or grid[ri][pushj] == "]"):
            pushj -= 1
        
        if grid[ri][pushj] == ".":
            # There is space to push
            for j in range(pushj, rj):
                grid[ri][j] = grid[ri][j + 1]
            grid[ri][rj] = "."
            rj -= 1

    elif d == "v":
        pushi += 1
        while pushi < len(grid) and grid[pushi][rj] == "O":
            pushi += 1
        
        if grid[pushi][rj] == ".":
            # There is space to push
            for i in range(pushi, ri, -1):
                grid[i][rj] = grid[i - 1][rj]
            grid[ri][rj] = "."
            ri += 1