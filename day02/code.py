with (open('input.txt', 'r') as input):
    data = input.readlines()

    games = {}
    p1 = 0
    p2 = 0
    limit = {'red': 12, 'green': 13, 'blue': 14}

    for line in data:
        line = line.strip().split(':')
        bags = line[-1].split(';')
        # get the game id for part 1
        curr_game = line[0].split()[-1]
        # mapping from each cube to its largest amount
        games[curr_game] = {'red': 0, 'green': 0, 'blue': 0}

        # for part 1
        valid = True
        # for part 2
        curr_min = 1

        for bag in bags:
            # get the bags
            bag = bag.strip().split(',')

            for cubes in bag:
                # first element is amount, second is color
                cubes = cubes.split()
                # if the current amount is the largest, change the amount in dictionary
                if int(cubes[0]) > games[curr_game][cubes[1]]:
                    # if it exceeds the limit, set valid to False
                    if int(cubes[0]) > limit[cubes[1]]:
                        valid = False
                    games[curr_game][cubes[1]] = int(cubes[0])

        # if the current game is valid, add the id to the result
        if valid:
            p1 += int(curr_game)

        # calculation for part 2
        for min_amount in games[curr_game].values():
            curr_min *= min_amount

        p2 += curr_min

    print(p1)
    print(p2)