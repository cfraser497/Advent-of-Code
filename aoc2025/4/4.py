import argparse

def print_grid(grid):
    print('\n'.join(grid))

def print_grid_with_accessible_rolls(grid, accessible_rolls):
    for i, j in accessible_rolls:
        old_row = list(grid[i])
        old_row[j] = 'x'
        grid[i] = ''.join(old_row)

    print_grid(grid)

def solve(file_input):
    grid = file_input
    accessible_rolls = []
    MAXIMUM_ROLLS = 4
    print_grid(file_input)
    
    def get_surrounding_rolls(grid, i, j, rolls):
        surrounding_rolls = 0
        for y in range(i - 1, i + 2):
            for x in range(j - 1, j + 2):
                if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and not (x == j and y == i):
                    # print(j, i, x, y)
                    if grid[y][x] == '@' and (y, x) not in accessible_rolls:
                        surrounding_rolls += 1
        return surrounding_rolls


    newly_accessible = True
    while newly_accessible:
        print("NEW: ", len(accessible_rolls))
        newly_accessible = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    surrounding_rolls = get_surrounding_rolls(grid, i, j)
                    if surrounding_rolls < MAXIMUM_ROLLS and (i, j) not in accessible_rolls:
                        accessible_rolls.append((i, j))
                        newly_accessible = True
                
                # check surroundings
    
    # debugging
    print('\n')
    print_grid_with_accessible_rolls(grid, accessible_rolls)
    return len(accessible_rolls)
    

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
