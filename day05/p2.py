def overlapped_lists(range_in, range_lists):
    to_check_range = [range_in]
    overlapped = []

    for tester in range_lists:
        for range_inp in to_check_range:
            if tester[0] <= range_inp[0] <= range_inp[1] <= tester[1]:
                overlapped.append([range_inp[0] - tester[0] + tester[2], range_inp[1] - tester[0] + tester[2]])
                range_inp[0], range_inp[1] = 0, 0

            elif tester[0] <= range_inp[0] < tester[1] < range_inp[1]:
                overlapped.append([range_inp[0] - tester[0] + tester[2], tester[2] + tester[1] - tester[0]])
                range_inp[0] = tester[1]

            elif range_inp[0] < tester[0] < tester[1] < range_inp[1]:
                overlapped.append([tester[2], range_inp[1] - tester[0] + tester[2]])
                to_check_range.append([range_inp[0], tester[0]])
                to_check_range.append([tester[1], range_inp[1]])

                range_inp[0], range_inp[1] = 0, 0

            elif range_inp[0] <= tester[0] <= range_inp[1] <= tester[1]:
                overlapped.append([tester[2], tester[2] + range_inp[1] - tester[0]])
                range_inp[1] = tester[0]

            else:
                continue

    for leftover in to_check_range:
        if leftover[1] - leftover[0] != 0:
            overlapped.append(leftover)

    return overlapped

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.read().split('\n\n')]

    seeds = lines[0].split(':')[1]
    seeds = [int(seed) for seed in seeds.split()]

    starting_point = []
    for idx_seed in range(0, len(seeds), 2):
        starting_point.append([seeds[idx_seed], seeds[idx_seed] + seeds[idx_seed + 1]])

    tracking = []
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
        starting_point = current_point[:]

    starting_point.sort(key = lambda x: x[0])

    print(starting_point[0][0])
