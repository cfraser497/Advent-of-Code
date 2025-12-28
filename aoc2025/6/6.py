import argparse
from functools import reduce

def solve(file_input):
    def remove_empties(l):
        nl = []
        spaces = []
        for e in l:
            if e != '':
                nl.append(e)
                spaces.append(0)
            else:
                print(spaces)
                spaces[-1] += 1
        return nl, spaces
    
    def get_func(symbol):
        match symbol:
            case '+':
                return lambda x, y: x + y
            case '-':
                return lambda x, y: x - y
            case '*':
                return lambda x, y: x * y
        
        raise ValueError(f"Invalid symbol {symbol}")

    # Parse operations
    operations, spaces = remove_empties(file_input[-1].split(' '))
    file_input = file_input[:-1]

    print(spaces)
    # Parse numbers
    numbers = []
    for row in file_input:
        num_str, _ = remove_empties(row.split(' '))
        numbers.append([int(x) for x in num_str])

    num_qs = len(numbers[0])
    answers = []
    for q in range(num_qs):
        func = get_func(operations[q])
        values = [numbers[i][q] for i in range(len(numbers))]
        answers.append(reduce(func, values))

    print(answers)
    return sum(answers)
    

def readFile(file):
    with open(f"{file}.txt", 'r') as f:
        file_contents = f.read().split('\n')

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
