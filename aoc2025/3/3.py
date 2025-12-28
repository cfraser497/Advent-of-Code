import argparse
from collections import defaultdict

def solve(file_input):
    def findLargestJoltage(bank, start_from):
        for joltage in range(9, -1, -1):
            for i, battery in enumerate(bank[start_from:]):
                if int(battery) == joltage:
                    return i + start_from, battery
        
        raise ValueError(f"Invalid bank {bank}")

    # PART 1
    # BATTERIES_REQUIRED = 2
    BATTERIES_REQUIRED = 12
    joltages = []
    
    for bank in file_input:
        # constuct bank dict
        recently_included_index = -1
        batteries = []
        for b in range(BATTERIES_REQUIRED - 1, -1, -1):
            recently_included_index, battery = findLargestJoltage(bank[:len(bank) - b], recently_included_index + 1)
            batteries.append(battery)

        joltages.append(int(''.join(batteries)))

    return sum(joltages)
    

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
