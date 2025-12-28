with open("day24.txt", "r") as file:
    inits, cs = file.read().strip().split("\n\n")

    inits = inits.split("\n")
    gates = {}
    for i in inits:
        g, v = i.split(": ")
        gates[g] = int(v)
    
    cs = cs.split("\n")
    connections = []
    totalZs = 0
    for c in cs:
        g1, op, g2, _, g3 = c.split(" ")
        connections.append((g1, op, g2, g3))
        # Calculate how many wires start with z
        if g3[0] == "z":
            totalZs += 1

computedZs = 0

print(totalZs)

while computedZs < totalZs:
    for g1, op, g2, g3 in connections:
        if g1 in gates and g2 in gates:
            match op:
                case "AND": gates[g3] = gates[g1] & gates[g2]
                case "OR": gates[g3] = gates[g1] | gates[g2]
                case "XOR": gates[g3] = gates[g1] ^ gates[g2]
            if g3[0] == "z":
                computedZs += 1
            connections.remove((g1, op, g2, g3))

# Organise the zs
total = 0
for i in range(totalZs):
    gate = f"z0{i}" if i < 10 else f"z{i}"
    total += gates[gate] * 2 ** i

print(total)