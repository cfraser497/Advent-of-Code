import argparse
from collections import defaultdict

OUT = 'out'
YOU = 'you'
SVR = 'svr'
FFT = 'fft'
DAC = 'dac'

def solve(file_input):
    graph = {}
    for device in file_input:
        device_name = device.split(":")[0]
        targets = device.split(":")[1].strip().split(" ")

        graph[device_name] = targets
    

    cache = defaultdict(dict)

    def dfs(node, path):
        def dict_key():
            dac = DAC if DAC in path else ''
            fft = FFT if FFT in path else ''
            return ''.join([dac, fft])

        if node in cache and dict_key() in cache[node]:
            return cache[node][dict_key()]
        
        if node == OUT:
            # uncomment for part 1
            # return 1
            return 1 if DAC in path and FFT in path else 0
        
        paths = 0
        for target in graph[node]:
            paths += dfs(target, path + [target])    
        

        cache[node][dict_key()] = paths
        return paths

    part1 = dfs(YOU, [YOU])
    part2 = dfs(SVR, [SVR])
    return (part1, part2)


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
