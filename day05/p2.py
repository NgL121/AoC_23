def overlapped_lists(range_in, range_lists): # range_in is a list of 2 numbers, the other is a list of lists
    to_check_range = [range_in] # list of lists
    overlapped = [] #list of lists

    for tester in range_lists:
        for range_inp in to_check_range:
            # if the current range is fully covered
            if tester[0] <= range_inp[0] <= range_inp[1] <= tester[1]:
                overlapped.append([range_inp[0] - tester[0] + tester[2], range_inp[1] - tester[0] + tester[2]])
                range_inp[0], range_inp[1] = 0, 0

            # if the next range (tester) is fully covered by the current range
            elif range_inp[0] < tester[0] < tester[1] < range_inp[1]:
                # get the overlapped
                overlapped.append([tester[2], range_inp[1] - tester[0] + tester[2]])

                # add the rest to the output
                to_check_range.append([range_inp[0], tester[0]]) # left range
                to_check_range.append([tester[1], range_inp[1]]) # right range

                # handle covered range
                range_inp[0], range_inp[1] = 0, 0

            # if not fully recovered: 2 cases
            elif range_inp[0] <= tester[0] <= range_inp[1] <= tester[1]:
                overlapped.append([tester[2], tester[2] + range_inp[1] - tester[0]])
                range_inp[1] = tester[0]

            elif tester[0] <= range_inp[0] < tester[1] < range_inp[1]:
                overlapped.append([range_inp[0] - tester[0] + tester[2], tester[2] + tester[1] - tester[0]])
                range_inp[0] = tester[1]

            # if 2 ranges don't have any overlaps
            else:
                continue

    # add the newly added range to the output (in the last 3 cases)
    for leftover in to_check_range:
        # only add if it's a valid range ([0,0] will not pass)
        if leftover[1] - leftover[0] != 0:
            overlapped.append(leftover)

    return overlapped # list of list

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.read().split('\n\n')]

    seeds = lines[0].split(':')[1]
    seeds = [int(seed) for seed in seeds.split()]

    starting_point = [] # start from the seeds, then soil -> fert -> wart, ... in the loop later
    for idx_seed in range(0, len(seeds), 2):
        starting_point.append([seeds[idx_seed], seeds[idx_seed] + seeds[idx_seed + 1]])

    tracking = [] # list of lists, includes mappings for soil, fert, ...
    lines = lines[1:]

    for line in lines:
        current = []
        line = line.split('\n')[1:]
        for val in line:
            val = [int(num) for num in val.split()]
            val = [val[1], val[1] + val[2], val[0], val[0] + val[2]]
            current.append(val)

        tracking.append(current)

    for track in tracking:
        current_point = []
        for start in starting_point:
            current_point += overlapped_lists(start, track)

        # seeds -> soils -> fert -> water -> ...
        starting_point = current_point[:]

    starting_point.sort(key = lambda x: x[0])

    print(starting_point[0][0])
