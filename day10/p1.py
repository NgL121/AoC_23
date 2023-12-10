pipes_to_directions = {
    '|': {'S': 'N', 'N' : 'S'},
    '-': {'W': 'E', 'E': 'W'},
    'L': {'N' : 'E', 'E': 'N'},
    'J': {'N': 'W', 'W': 'N'},
    '7': {'S': 'W', 'W': 'S'},
    'F': {'S': 'E', 'E': 'S'}
}

pos_to_dir = {
    (0, 1): 'S',
    (0, -1): 'N',
    (-1, 0): 'W',
    (1, 0): 'E'
}

dir_to_pos = {dir: pos for pos, dir in pos_to_dir.items()}
print(dir_to_pos)

def get_position(pos_prev, pos_curr):
    prev_x, prev_y = pos_prev
    curr_x, curr_y = pos_curr
    pos_diff = (prev_x - curr_x, prev_y - curr_y)
    return pos_to_dir[pos_diff]

def dir_to_val(pos_curr, direction):
    step = dir_to_pos[direction.upper()]
    pos_next = (pos_curr[0] + step[0], pos_curr[1] + step[1])
    if -1 in pos_next:
        return None
    return pos_next

def get_next (prev, current): # return current, next
    pipe = MAZE[current[1]][current[0]]

    start_pos = get_position(prev, current)
    output_dir = pipes_to_directions[pipe][start_pos]
    end = dir_to_val(current, output_dir)

    return current, end

with open('input.txt', 'r') as data:
    MAZE = [line.strip() for line in data.readlines()]
    print(MAZE)

    running = True
    for idx_row, row in enumerate(MAZE):
        for idx_col, col in enumerate(row):
            if col == 'S':
                start_pos = (idx_col, idx_row)
                break

    start_north = dir_to_val(start_pos, 'N')
    start_south = dir_to_val(start_pos, 'S')
    start_west = dir_to_val(start_pos, 'W')
    start_east = dir_to_val(start_pos, 'e')

    start_pipe_pos = ()
    if start_north and MAZE[start_north[1]][start_north[0]] in ['7', '|']:
        start_pipe_pos = start_north
    elif start_south and MAZE[start_south[1]][start_south[0]] in ['L', '|']:
        start_pipe_pos = start_south
    elif start_west and MAZE[start_west[1]][start_west[0]] in ['F', '-']:
        start_pipe_pos = start_west
    elif start_east and MAZE[start_east[1]][start_east[0]] in ['7', '-']:
        start_pipe_pos = start_east

    prev = start_pos
    pointer = start_pipe_pos
    step = 1
    while MAZE[pointer[1]][pointer[0]] != 'S':
        prev, pointer = get_next(prev, pointer)
        step += 1

    print(step//2)