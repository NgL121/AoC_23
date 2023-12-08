from math import lcm

def get_next(idx):
    idx = idx % len(DIRECTIONS)
    direct = DIRECTIONS[idx]

    if direct == 'L':
        return 0

    return 1

with open('input.txt', 'r') as data:
    lines = data.read().split('\n\n')

    DIRECTIONS = lines[0]
    NODES_MAPPING = {}
    start = []

    nodes = lines[1].split('\n')
    for node in nodes:
        node = node.split(' = ')
        next_node = node[1][1:-1].split(', ')
        NODES_MAPPING[node[0]] = next_node
        if node[0].endswith('A'):
            start.append(node[0])

    pointer = ''

    steps = []
    for node in start:
        pointer = node
        idx = 0
        step = 0
        while not pointer.endswith('Z'):
            pointer = NODES_MAPPING[pointer][get_next(idx)]
            idx += 1
            step += 1
        steps.append(step)
        if node == 'AAA' and pointer != 'ZZZ':
            pointer = NODES_MAPPING[pointer][get_next(idx)]
            idx += 1
            step += 1
        if node == 'AAA' and pointer == 'ZZZ':
            print('part 1:', step)

    p2_lcm = steps[0]
    for step in steps[1:]:
        p2_lcm = lcm(p2_lcm, step)

    print('part 2:', p2_lcm)