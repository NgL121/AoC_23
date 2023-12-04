with open('input.txt', 'r') as data:
    data = [line.strip() for line in data.readlines()]
    output = 0
    count_copies = [0] * (len(data) +1)

    # iterate over every line
    for line in data:

        # divide it into 2 parts
        line = line.split(':')
        card_id = int(line[0].split()[-1])
        line = line[1]

        count_copies[card_id] += 1

        line = line.split('|')
        # get the winning card
        winning_numbers = [int(num) for num in line[0].split()]

        numbers = [int(num) for num in line[1].split()]

        exp = 0
        curr_point = 0

        for num in numbers:
            if num in winning_numbers:
                curr_point = 2**exp
                exp += 1

        if curr_point > 0:
            for idx in range(card_id + 1, card_id + exp + 1):
                count_copies[idx] += 1*count_copies[card_id]

        output += curr_point

    print(output)
    print(sum(count_copies))