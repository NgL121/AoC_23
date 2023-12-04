with open('input.txt', 'r') as data:
    data = [line.strip() for line in data.readlines()]
    output = 0
    count_copies = [0] * len(data)
    print(count_copies)

    # iterate over every line
    for line in data:
        # divide it into 2 parts
        line = line.split(':')[1]
        line = line.split('|')
        # get the winning card
        winning_numbers = [int(num) for num in line[0].split()]
        # print(winning_numbers)

        numbers = [int(num) for num in line[1].split()]
        # print(numbers)

        exp = 0
        curr_point = 0

        for num in numbers:
            if num in winning_numbers:
                curr_point = 2**exp
                exp += 1

        output += curr_point

    print(output)