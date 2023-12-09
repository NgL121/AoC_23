with open('input.txt', 'r') as data:
    lines = data.readlines()

    output = 0
    for line in lines:
        history = []
        line = [int(num) for num in line.split()]

        temp = line
        while list(set(temp)) != [0]:
            curr_val = temp[0]

            for idx, num in enumerate(temp):
                if idx == 0:
                    continue

                point = num - curr_val
                curr_val = num
                temp[idx] = point

                # end of a line
                if idx == len(temp) - 1:
                    history.append(temp[0])

            temp.pop(0)

        history.append(0)
        calc = history[-1]
        for i in range(len(history) - 2, -1, -1):
            calc = history[i] - calc
        output += calc

    print(output)