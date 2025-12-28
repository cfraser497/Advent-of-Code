from itertools import count

with open("day14.txt", "r") as file:
    robots = file.read().strip().split('\n')

NUM_ITER = 100
BOARD_X = 101
BOARD_Y = 103


def getNums(s):
    ns = s.split("=")[1]
    x, y = ns.split(",")
    return (int(x), int(y))

def printGrid(g):
    for r in g:
        print(r)

rs = []

for r in robots:
    robot = []
    p, v = r.split(" ")

    robot.append(getNums(p))
    robot.append(getNums(v))

    rs.append(robot)


# Run the simulation
for num_iters in count(1):
    futureRs = []
    
    for (x, y), (vx, vy) in rs:
        newx = (x + num_iters * vx) % BOARD_X
        newy = (y + num_iters * vy) % BOARD_Y

        futureRs.append((newx, newy))

    if num_iters == NUM_ITER:
        rs100 = futureRs


    if len(futureRs) == len(set(futureRs)):
        grid = [[0 for _ in range(BOARD_X)] for _ in range(BOARD_Y)]

        for (rx, ry) in futureRs:
            grid[ry][rx] += 1

        for i in range(BOARD_Y):
            for j in range(BOARD_X):
                if grid[i][j] == 0:
                    grid[i][j] = "."
                else:
                    grid[i][j] = str(grid[i][j])
            grid[i] = "".join(grid[i])
            
        print(f"ITERATION: {num_iters}")
        printGrid(grid)
        print("\n")

        break

futureRs = rs100

# Calculate safety score
q1, q2, q3, q4 = 0, 0, 0, 0
for (rx, ry) in futureRs:
    if rx < (BOARD_X - 1) // 2 and ry < (BOARD_Y - 1) // 2:
        q1 += 1
    elif rx > (BOARD_X - 1) // 2 and ry < (BOARD_Y - 1) // 2:
        q2 += 1
    elif rx < (BOARD_X - 1) // 2 and ry > (BOARD_Y - 1) // 2:
        q3 += 1
    elif rx > (BOARD_X - 1) // 2 and ry > (BOARD_Y - 1) // 2:
        q4 += 1

res = q1 * q2 * q3 * q4

print(res)

