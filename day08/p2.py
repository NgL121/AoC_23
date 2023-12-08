from math import lcm

with open('input.txt', 'r') as data:
    line = data.read().split('\n\n')

    directions = line[0]
    nodes_list = line[1].split('\n')
    nodes = {}

    starting_nodes = []
    for node in nodes_list:
        node = node.split(' = ')
        node[1] = node[1][1:-1].split(',')
        nodes[node[0].strip()] = [node[1][0].strip(), node[1][1].strip()]
        if node[0].strip()[-1] == 'A':
            starting_nodes.append(node[0].strip())

    steps = []
    for current_node in starting_nodes:
        cont = True
        step = 0
        idx = 0
        while idx < len(directions):
            direct = directions[idx]

            if direct == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

            if current_node.endswith('Z'):
                cont = False
                step += 1
                steps.append(step)
                break

            step += 1
            if idx == len(directions) - 1:
                idx = 0
            else:
                idx += 1
        if not cont:
            continue

    output = steps[0]

    for step in steps[1:]:
        output = lcm(output, step)

    print(output)