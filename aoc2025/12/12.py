import argparse

def solve(file_input):
    shapes = {}
    regions = []

    i = 0
    line = file_input[i]
    while 'x' not in line.split(":")[0]:
        shapes[i] = line.split(':')[1][1:].split('\n')
        i += 1
        line = file_input[i]

    regions_raw = line.split('\n')
    for region in regions_raw:
        dims = list(map(int, region.split(':')[0].split('x')))
        pieces = list(map(int, region.split(':')[1].strip().split(' ')))
        regions.append((dims, pieces))
    
    shape_area = {}
    for i, shape in shapes.items():
        area = 0
        for row in shape:
            for c in row:
                if c == '#':
                    area += 1

        shape_area[i] = area

    # print(shapes)
    # print(regions)
    valid_regions = 0
    for dims, pieces in regions:
        region_area = dims[0] * dims[1]
        total_shape_area = 0
        
        for shape_index, count in enumerate(pieces):
            # print(count)
            # print(shape_area)
            # print(shape_index)
            total_shape_area += count * shape_area[shape_index]

        if total_shape_area <= region_area:
            valid_regions += 1

    return valid_regions
    

def readFile(file):
    with open(f"{file}.txt", 'r') as f:
        file_contents = f.read().split('\n\n')

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
