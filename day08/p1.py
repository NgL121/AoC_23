with open('input.txt', 'r') as data:
    line = data.read().split('\n\n')

    directions = line[0]
    print(directions)
    nodes_list = line[1].split('\n')
    nodes = {}


    for node in nodes_list:
        node = node.split(' = ')
        node[1] = node[1][1:-1].split(',')
        nodes[node[0].strip()] = [node[1][0].strip(), node[1][1].strip()]

    idx = 0
    step = 0
    current_node = 'AAA'
    while idx < len(directions):

        direct = directions[idx]

        if direct == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]

        if current_node == 'ZZZ':
            step += 1
            break

        step += 1
        if idx == len(directions) - 1:
            idx = 0
        else:
            idx += 1

    print(step)