from collections import defaultdict

grid = []

with open("day6.txt", "r") as file:
    grid = file.read().split()

# Find the start of the guard

start = ()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^':
            start = (i, j)
          
print(start)

# Run the simulaton

# Map containing (i, j) -> [direction]
# direction: 0: up, 1: right, 2: down, 3: left
visited = defaultdict(list)
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
heading = 0
i, j = start

while 0 < i < len(grid) - 1 and 0 < j < len(grid[0]) - 1:
    visited[(i, j)].append(heading)
    di, dj = directions[heading]

    nexti, nextj = i + di, j + dj

    if grid[nexti][nextj] == '#':
        # Turn
        heading = (heading + 1) % len(directions)
    else:
        # Move forward
        i, j = nexti, nextj

visited[(i, j)].append(heading)
print(len(visited))

## PART 2
visited[(i, j)].remove(heading)

obs = set()

for (starti, startj), headings in visited.items():
    for h in headings:
        # Place an obstruction in front of the guard
        di, dj = directions[h]
        obsi, obsj = starti + di, startj + dj
    
        if grid[obsi][obsj] == '#' or (obsi, obsj) in obs:
            continue

        # Update grid with new obstacle
        row = list(grid[obsi])
        row[obsj] = '#'
        grid[obsi] = ''.join(row)

        # Same map structure as visited
        wouldVisit = defaultdict(list)

        # Run the simulation
        i, j = start
        heading = 0
        
        while 0 < i < len(grid) - 1 and 0 < j < len(grid[0]) - 1:
            if heading in wouldVisit[(i, j)]:
            # we have been here before -> we are in a loop
                obs.add((obsi, obsj))
                break
            
            wouldVisit[(i, j)].append(heading)
            di, dj = directions[heading]

            nexti, nextj = i + di, j + dj

            if grid[nexti][nextj] == '#':
                # Turn
                heading = (heading + 1) % len(directions)
            else:
                # Move forward
                i, j = nexti, nextj

        # Change back the grid
        row = list(grid[obsi])
        row[obsj] = '.'
        grid[obsi] = ''.join(row)


print(len(obs))