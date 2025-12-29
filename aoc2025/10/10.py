import argparse
from collections import deque

# idea 1: BFS
# idea 2: Linear Algebra

ON = '#'
PART1 = False

def parse_machines(file_input):
    machines = []
    
    for line in file_input:
        indicators = line.split(']')[0][1:]
        indicators = [i == ON for i in indicators]
        
        buttons = line.split(' ')[1:-1]
        buttons = [list(map(int, b[1:-1].split(','))) for b in buttons]
        buttons.sort(key=lambda bs: len(bs), reverse=True)

        joltage_reqs = line.split('{')[1][:-1]
        joltage_reqs = [int(j) for j in joltage_reqs.split(',')]

        machine = (indicators, buttons, joltage_reqs)
        machines.append(machine)
    return machines

def solve(file_input):
    machines = parse_machines(file_input)
    total_presses = 0

    if PART1:
        for machine in machines:
            print("MACHINE", machine)
            indicators, buttons, joltages = machine
            initial_state = [False for _ in indicators]
            if initial_state == indicators:
                continue
            
            q = deque([(initial_state, [])])

            while q:
                state, presses = q.popleft()

                for b in buttons:
                    new_state = state.copy()
                    # switch the lights
                    for light in b:
                        
                        new_state[light] = not state[light]

                    if new_state == indicators:
                        print(presses + [b], len(presses) + 1)
                        total_presses += (len(presses) + 1)
                        q = None
                        break

                    q.append((new_state, presses + [b]))


    else:
        # too slow T_T
        for machine in machines:
            print("MACHINE", machine)
            _, buttons, joltages = machine
            initial_state = [0 for _ in joltages]
            if initial_state == joltages:
                continue
            
            q = deque([(initial_state, [])])
            seen = {tuple(initial_state)}

            while q:
                state, presses = q.popleft()

                for b in buttons:
                    new_state = state.copy()
                    # switch the lights
                    for light in b:
                        new_state[light] += 1

                    new_presses = presses + [b]
                    if new_state == joltages:
                        print(new_presses, len(new_presses))
                        total_presses += (len(new_presses))
                        q = None
                        break

                    # only append valid states
                    valid = [j <= joltages[i] for i, j in enumerate(new_state)]
                    if all(valid) and tuple(new_state) not in seen:
                        # print(new_state, len(new_presses))
                        seen.add(tuple(new_state))
                        q.append((new_state, new_presses))

    return total_presses
    

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
