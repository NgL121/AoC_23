with open ('test.txt', 'r') as data:
    lines = data.read().split('\n\n')

    seeds = lines[0].split(':')
    seeds = [int(seed) for seed in seeds[1].split()]

    pointer = seeds

    for line in lines[1:]:
        line = line.split('\n')
        check_list = []
        for find in pointer:
            found = False
            for maps in line[1:]:
                maps = [int(num) for num in maps.split()]
                if find in range(maps[1], maps[1] + maps[2]):
                    check_list.append(maps[0] + find - maps[1])
                    found = True

            if not found:
                check_list.append(find)

        pointer = check_list

    print(min(pointer))