import argparse
import math
from functools import reduce

def solve(file_input):
    coords = [list(map(int, x.split(','))) for x in file_input]

    NUM_CONNECTIONS = 10000000000000
    NUM_BIGGEST = 3
    distances = []

    for i, (x1, y1, z1) in enumerate(coords[:-1]):
        for x2, y2, z2 in coords[i + 1:]:
            d2 = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            d = math.sqrt(d2)
            distances.append((d, (x1, y1, z1), (x2, y2, z2)))

    distances.sort()

    # Connect the circuits
    graph = {}
    for x, y, z in coords:
        graph[(x, y, z)] = {(x, y, z)}

    for i in range(NUM_CONNECTIONS):
        d, c1, c2 = distances[i]
        graph[c1] = graph[c1].union(graph[c2])
        if len(graph[c1]) == len(coords):
            # part 2 - completed graph
            return c1[0] * c2[0]
        for c in graph[c1]:
            graph[c] = graph[c1]

    # Get biggest circuits

    circuit_sizes = sorted(list(map(len, graph.values())))
    biggest = []
    i = len(circuit_sizes) - 1
    for _ in range(NUM_BIGGEST):
        biggest.append(circuit_sizes[i])
        i -= circuit_sizes[i]

    print(biggest)
    return reduce(lambda x, y: x * y, biggest)
    

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
