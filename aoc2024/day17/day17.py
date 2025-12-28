import math
from itertools import count

with open("day17.txt", "r") as file:
    rs, p = file.read().strip().split("\n\n")

    sa, sb, sc = rs.split("\n")
    ra, rb, rc = int(sa.split(" ")[2]), int(sb.split(" ")[2]), int(sc.split(" ")[2])

    p = p.split(" ")[1].split(",")
    p = [int(i) for i in p]


# ra, rb, rc = 117440, 0, 0
# p = [0,3,5,4,3,0]

print(ra)
print(rb)
print(rc)

print(p)

def combo(op, ra, rb, rc):
    match op:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc
        case _:
            raise IndexError


for raIdx in count(1):
    if raIdx % 100000 == 0:
        print(raIdx)
    ip = 0
    outIdx = 0
    out = []
    ra = raIdx

    while ip < len(p):
        opcode = p[ip]
        operand = p[ip + 1]
        match p[ip]:
            case 0:
                # adv
                denom = combo(operand, ra, rb, rc)
                ra = math.trunc(ra / (2 ** denom))
            case 1:
                # bxl
                rb = rb ^ operand
            case 2:
                # bst
                rb = combo(operand, ra, rb, rc) % 8
            case 3:
                #jnz
                if ra != 0:
                    ip = operand
                    continue
            case 4:
                # bxc
                rb = rb ^ rc
            case 5:
                # out
                output = combo(operand, ra, rb, rc) % 8
                if output != p[outIdx] or len(out) > len(p):
                    # Not going to produce the same program
                    break
                out.append(str(output))
                outIdx += 1
            case 6:
                # bdv
                denon = combo(operand, ra, rb, rc)
                rb = math.trunc(ra / (2 ** denom))
            case 7:
                # cdv
                denom = combo(operand, ra, rb, rc)
                rc = math.trunc(ra / (2 ** denom))
            case _:
                raise IndexError
                
        ip += 2

    out = [int(i) for i in out]
    if p == out:
        print(f"RAIDX: {raIdx}")
        print(out)
        break

print(out)