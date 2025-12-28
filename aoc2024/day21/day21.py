from collections import deque

with open("day21.txt", "r") as file:
    codes = file.read().strip().split("\n")

NUMERIC_KEYPAD = {
    "A": [("0", "<"), ("3", "^")],
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("A", "v"), ("2", "<"), ("6", "^")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
}

DIRECTONAL_KEYPAD = {
    "A": [("^", "<"), (">", "v")],
    "^": [("v", "v"), ("A", ">")],
    "<": [("v", ">")],
    "v": [("^", "^"), ("<", "<"), (">", ">")],
    ">": [("A", "^"), ("v", "<")],
}


print(codes)

# for c in codes:
def getInputs(KEYPAD, codes):
    res = []
    minResLength = float('inf')

    for code in codes:
        possInputs = [""]
        for i, l in enumerate(code):
            inputs = []
            minInputLength = float('inf')
            for pi in possInputs:
                # BFS to find shortest path
                # Staring element
                start = "A" if i - 1 < 0 else code[i - 1]
                Q = deque([(start, pi)])

                while Q:
                    loc, path = Q.popleft()
                    if loc == l:
                        # We are here
                        path += "A"
                        if len(path) < minInputLength:
                            inputs = []
                            minInputLength = len(path)
                        inputs.append(path)
                        continue
                    if len(path) >= minInputLength:
                        continue
                    for location, pathSymbol in KEYPAD[loc]:
                        Q.append((location, path + pathSymbol))
                
                possInputs = inputs

        if minInputLength < minResLength:
            res = inputs
        elif minInputLength == minResLength:
            res.extend(inputs)
        minResLength = min(minInputLength, minResLength)
        
    return res


complexity = 0
for code in codes:
    leadingNo = int(code[:-1])

    inputs = getInputs(NUMERIC_KEYPAD, [code])
    secondInputs = getInputs(DIRECTONAL_KEYPAD, inputs)
    thirdInputs = getInputs(DIRECTONAL_KEYPAD, secondInputs)

    complexity += leadingNo * len(thirdInputs[0])

print(complexity)