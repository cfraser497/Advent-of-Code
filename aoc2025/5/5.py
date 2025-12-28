import argparse

def solve(file_input):
    ranges_str = file_input[0].split()
    ids = file_input[1].split()
    
    ranges = []
    for r in ranges_str:
        f, l = r.split('-')
        ranges.append((int(f), int(l)))

    fresh = []

    for ingredient_id in ids:
        for f, l in ranges:
            if f <= int(ingredient_id) <= l:
                fresh.append(ingredient_id) 
                break

    print(fresh)

    # part 2
    ranges.sort()
    print(ranges)
    flattened_ranges = []

    for i, pair in enumerate(ranges):
        f, l = pair
        if i == 0:
            flattened_ranges.append([f, l])
            continue

        if f > flattened_ranges[-1][1]:
            flattened_ranges.append([f, l])
            continue

        if l > flattened_ranges[-1][1]:
            flattened_ranges[-1][1] = l

    total_fresh = 0
    for f, l in flattened_ranges:
        total_fresh += l - f + 1
    
    print(flattened_ranges)
    return total_fresh
    

def readFile(file):
    with open(f"{file}.txt", 'r') as f:
        file_contents = f.read().split('\n\n')

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
