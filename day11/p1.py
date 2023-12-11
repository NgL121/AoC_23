def distance(pos_1, pos_2):
    return abs(pos_1[0] - pos_2[0]) + abs(pos_1[1] - pos_2[1])

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    rows = []
    cols = []

    for idx_line, line in enumerate(lines):
        rows.append(line)
        if '#' not in line:
            rows.append(line)

    for col in range(len(lines[0])):
        current = ''
        for row in rows:
            current += row[col]
        cols.append(current)
        if '#' not in current:
            cols.append(current)

    galaxy = []
    for idx in range(len(cols[0])):
        current = ''
        for col in cols:
            current += col[idx]
        galaxy.append(current)

    uni_list = []
    for y, r in enumerate(galaxy):
        for x, c in enumerate(r):
            if galaxy[y][x] == '#':
                uni_list.append((y + 1,x + 1))

    output = 0
    for idx, uni in enumerate(uni_list[:-1]):
        for next_uni in uni_list[idx+1:]:
            output += distance(uni, next_uni)

    print(output)