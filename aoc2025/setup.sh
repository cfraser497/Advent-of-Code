#!/usr/bin/env bash

for i in {3..12}; do
    mkdir -p "$i"

    # Create empty input files
    touch "$i/$i.txt"
    touch "$i/test.txt"

    # Create Python file with template
    cat > "$i/$i.py" << EOF
import argparse

def solve(file_input):
    
    return 0
    

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
EOF

done
