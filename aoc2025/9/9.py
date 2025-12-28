import argparse

RED = '#'
GREEN = 'X'
OTHER = '.'
EMPTY = '_'

def print_grid(grid):
    print('\n'.join([''.join(row) for row in grid]))

def solve(file_input):
    coords = [tuple(map(int, c.split(','))) for c in file_input]

    # minX = min(coords, key=lambda c: c[0])[0]
    # maxX = max(coords, key=lambda c: c[0])[0]
    # minY = min(coords, key=lambda c: c[1])[1]
    # maxY = max(coords, key=lambda c: c[1])[1]

    # coords = list(map(lambda c: (c[0] - minX + 1, c[1] - minY + 1), coords))
    # maxX = maxX - minX + 1
    # maxY = maxY - minY + 1
    # minX, minY = 1, 1

    # grid = [[EMPTY for _ in range(maxX + 2)] for _ in range(maxY + 2)]
   
    # for i, (ccx, ccy) in enumerate(coords):
    #     grid[ccy][ccx] = RED

    #     # fill in green edges
    #     pcx, pcy = coords[i - 1]
    #     minx, maxx = min(ccx, pcx), max(ccx, pcx)
    #     miny, maxy = min(ccy, pcy), max(ccy, pcy)

    #     # print(coords[i + 1], coords[i], ccx, pcx, ccy, pcy)
    #     if ccy == pcy:
    #         grid[ccy][minx + 1: maxx] = [GREEN for _ in range(maxx - minx - 1)]
    #     else:
    #         for j in range(miny + 1, maxy):
    #             grid[j][ccx] = GREEN

    # # fill in edges
    # seen = set()
    # directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    # def dfs(c):
    #     x, y = c
    #     grid[y][x] = OTHER
    #     seen.add((x, y))
    #     for dx, dy in directions:
    #         nx, ny = x + dx, y + dy
    #         if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx, ny) not in seen and grid[ny][nx] != RED and grid[ny][nx] != GREEN:
    #             dfs((nx, ny))

    # dfs((0, 0))
    
    # # fill in empties with green
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == EMPTY:
    #             grid[i][j] = GREEN
    # print_grid(grid)

    allSides = []

    for i, (x1, y1) in enumerate(coords):
        x2, y2 = coords[i - 1]
        allSides.append(((x2, y2), (x1, y1)))

    print(coords)
    print(allSides)

    def isValidRect(x1, y1, x2, y2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        isValid = True

        for (asx1, asy1), (asx2, asy2) in allSides:
            asx1, asx2 = min(asx1, asx2), max(asx1, asx2)
            asy1, asy2 = min(asy1, asy2), max(asy1, asy2)

            # check this side is valid
            # 1. is any point inside the recetange?
            if (x1 < asx1 < x2 and y1 < asy1 < y2) or (x1 < asx2 < x2 and y1 < asy2 < y2):
                return False

            # 2. is the line cutting through the rectangle?
            # 2a. line start above the rectangle
            if x1 < asx1 < x2 and asy1 <= y1:
                isValid &= asy2 <= y1

            # 2b. line start below the rectangle
            if x1 < asx2 < x2 and asy2 >= y2:
                isValid &= asy1 >= y2

            # 2c. line to the left of rectangle
            if y1 < asy1 < y2 and asx1 <= x1:
                isValid &= asx2 <= x1

            # 2d. line to the right of rectangle
            if y1 < asy2 < y2 and asx2 >= y2:
                isValid &= asx1 >= x2

            if not isValid:
                return False
            
        return isValid            

    maxArea = 0
    for i, (x1, y1) in enumerate(coords[:-1]):
        for x2, y2 in coords[i + 1:]:
            if isValidRect(x1, y1, x2, y2):
                maxArea = max(maxArea, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    return maxArea
    

def readFile(file):
    with open(f"{file}.txt", 'r') as f:
        file_contents = f.read().split()

    return file_contents

def main():
    parser = argparse.ArgumentParser(description=f"Solve AOC Day {__file__.split('.')[0]}")
    parser.add_argument("--input", default=".txt", help="Path to input .txt file")
    args = parser.parse_args()

    file = readFile(args.input)

    ans = solve(file)

    print(ans)
    

if __name__ == "__main__":
    main()
