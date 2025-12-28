import argparse

def solve(file_input):
    DIAL_SIZE = 100

    rotations = file_input

    dial = 50
    zeros = 0

    for r in rotations:
        direction, clicks = r[0], int(r[1:])

        if direction == 'R':
            dial = dial + clicks
            zeros += dial // DIAL_SIZE
            if (dial // DIAL_SIZE != 0):
                print(r)
        elif direction == 'L':
            startDial = dial
            dial = dial - clicks
            if startDial == 0:
                zeros += abs((dial - 1) // DIAL_SIZE) - 1
            else:
                zeros += abs((dial - 1) // DIAL_SIZE)
            if (abs((dial - 1) // DIAL_SIZE) != 0 and startDial != 0):
                print((r, dial))
        else:
            raise ValueError("Unrecognised Direction")
        # if dial == 0:
        #     zeros += 1

        dial %= DIAL_SIZE

    return zeros

def readFile(file):
    with open(f"{file}.txt", 'r') as f:
        file_contents = f.read().split()

    return file_contents

def main():
    parser = argparse.ArgumentParser(description="Solve AOC Day 1")
    parser.add_argument("--input", default=".txt", help="Path to input .txt file")
    args = parser.parse_args()

    file = readFile(args.input)

    ans = solve(file)

    print(ans)
    

if __name__ == "__main__":
    main()
