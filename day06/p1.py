with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    times = lines[0]
    times = times.split(':')[1].split()
    times = [int(t) for t in times]

    distance = lines[1]
    distance = [int(d) for d in distance.split(':')[1].split()]

    time_dist_pairs = {}
    for t, d in zip(times, distance):
        time_dist_pairs[t] = d

    output = 1

    for t in times:
        start = 1
        end = t - 1

        while start < t:
            if start*(t - start) > time_dist_pairs[t]:
                break
            start += 1

        end = t - start
        print(start, end)
        output *= (end-start) + 1

    print(output)
