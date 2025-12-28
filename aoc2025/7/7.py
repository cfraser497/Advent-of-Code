import argparse
from collections import defaultdict

def print_grid(grid):
    print('\n'.join(grid))

def solve(grid):
    beams = {grid[0].find('S')}
    timelines = defaultdict(int)
    timelines[grid[0].find('S')] = 1
    splits = 0
    for row in grid[1:]:
        new_set = set()
        # print(timelines)
        for beam in beams:
            if row[beam] == '^':
                if beam > 0:
                    new_set.add(beam - 1)
                    timelines[beam - 1] += timelines[beam]
                if beam < len(grid[0]) - 1:
                    new_set.add(beam + 1)
                    timelines[beam + 1] += timelines[beam]
                timelines[beam] = 0
                splits += 1
            else:
                new_set.add(beam)

        beams = new_set

    
    return splits, sum(timelines.values())
    

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
