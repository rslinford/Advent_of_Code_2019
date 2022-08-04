def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        path_a, path_b = f.read().strip().split('\n')
        path_a = path_a.strip()
        path_b = path_b.strip()
        path_a = path_a.split(',')
        path_b = path_b.split(',')
        return path_a, path_b

def trace_path(path):
    rval = []
    cur_pos = (0, 0)
    rval.append(cur_pos)
    for direction in path:
        lrud = direction[0]
        distance = int(direction[1:])
        prev_pos = cur_pos
        match lrud:
            case 'L':
                cur_pos = (cur_pos[0] - distance, cur_pos[1])
                sign = (cur_pos[0] - prev_pos[0]) // abs (cur_pos[0] - prev_pos[0])
                for x in range(prev_pos[0] + sign, cur_pos[0] + sign, sign):
                    rval.append((x, cur_pos[1]))
            case 'R':
                cur_pos = (cur_pos[0] + distance, cur_pos[1])
                sign = (cur_pos[0] - prev_pos[0]) // abs(cur_pos[0] - prev_pos[0])
                for x in range(prev_pos[0] + sign, cur_pos[0] + sign, sign):
                    rval.append((x, cur_pos[1]))
            case 'U':
                cur_pos = (cur_pos[0], cur_pos[1] - distance)
                sign = (cur_pos[1] - prev_pos[1]) // abs(cur_pos[1] - prev_pos[1])
                for y in range(prev_pos[0] + sign, cur_pos[1] + sign, sign):
                    rval.append((cur_pos[0], y))
            case 'D':
                cur_pos = (cur_pos[0], cur_pos[1] + distance)
                sign = (cur_pos[1] - prev_pos[1]) // abs(cur_pos[1] - prev_pos[1])
                for y in range(prev_pos[0] + sign, cur_pos[1] + sign, sign):
                    rval.append((cur_pos[0], y))
            case _:
                print(f'Was expecting L, R, U, or D but got {lrud}')

    return rval



def find_all_intersections(a, b):
    # scan for points in common
    rval = []
    for p1 in a:
        for p2 in b:
            if p1 == p2:
                rval.append(p1)
                print(f'Points so far in common: {len(rval)}')
    return rval



a, b = read_puzzle_data('Day_03_data.txt')
a = trace_path(a)
b = trace_path(b)
# print(a, '\n', b)
intersections = find_all_intersections(a, b)
# print(f'Lines intersect at {intersections}')


def manhattan_distance(intersection):
    return abs(intersection[0]) + abs(intersection[1])

smallest_distance = float('inf')
for intersection in intersections:
    if intersection == (0, 0):
        continue
    if manhattan_distance(intersection) < smallest_distance:
        smallest_distance = manhattan_distance(intersection)
print(f'The smallest distance from origin: {smallest_distance}')
