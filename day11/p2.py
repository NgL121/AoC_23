def distance(pos_1, pos_2):
    diff_X = 0
    diff_Y = 0

    for y in ROW_TO_EXPAND:
        if min(pos_1[0], pos_2[0]) < y < max(pos_1[0], pos_2[0]):
            diff_X += EXPAND - 1

    for x in COL_TO_EXPAND:
        if min(pos_1[1], pos_2[1]) < x < max(pos_1[1], pos_2[1]):
            diff_Y += EXPAND - 1

    return abs(pos_1[0] - pos_2[0]) + diff_X + abs(pos_1[1] - pos_2[1]) + diff_Y


with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    rows = []
    cols = []

    EXPAND = 1000000

    ROW_TO_EXPAND = []
    for idx_line, line in enumerate(lines):
        rows.append(line)
        if '#' not in line:
            ROW_TO_EXPAND.append(idx_line + 1)

    COL_TO_EXPAND = []
    for col in range(len(lines[0])):
        current = ''
        for row in rows:
            current += row[col]
        cols.append(current)
        if '#' not in current:
            COL_TO_EXPAND.append(col + 1)

    uni_list = []
    for y, r in enumerate(lines):
        for x, c in enumerate(r):
            if lines[y][x] == '#':
                uni_list.append((y + 1,x + 1))

    output = 0
    for idx, uni in enumerate(uni_list[:-1]):
        for next_uni in uni_list[idx+1:]:
            output += distance(uni, next_uni)

    print(output)