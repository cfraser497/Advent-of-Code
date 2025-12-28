import argparse

def solve(file_input):
    def isInvalid(i):
        i = str(i)

        for l in range(1, len(i)):
            if len(i) % l != 0:
                continue
            parts = [i[x:x+l] for x in range(0, len(i), l)]

            if len(set(parts)) == 1:
                return True
            
        return False


    rs = file_input[0].split(",")
    ranges = []
    for r in rs:
        f, l = r.split('-')
        ranges.append((int(f), int(l)))
    
    invalidIds = []
    for f, l in ranges:
        for i in range(f, l + 1):
            # i = str(i)
            # if len(i) % 2 != 0:
            #     continue

            # mid = len(i) // 2

            # if i[:mid] == i[mid:]:
            #     invalidIds.append(int(i))

            if isInvalid(i):
                invalidIds.append(i)

    return sum(invalidIds)
    

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
