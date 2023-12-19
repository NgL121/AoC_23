import re

class Part:
    def __init__(self, x, m, a, s):
        self.mapping = {'x': x, 'm': m, 'a': a, 's': s}

    @classmethod
    def process_line(cls, line):
        x, m, a, s = re.findall(r'x=(\d+),m=(\d+),a=(\d+),s=(\d+)', line)[0]
        return cls(int(x),int(m),int(a),int(s))

    def check_con(self, con_list):
        for idx, con in enumerate(con_list[:-1]):
            if check_sub_con(self.mapping[con[0]], con):
                return con[2]
        return con_list[-1]

    def get_sum(self):
        return sum(self.mapping.values())


def check_sub_con(part, cond):
    if type(cond[1]) == int:
        if part > cond[1]:
            return True
        return False
    else:
        if part in range(cond[1][0], cond[1][1]):
            return True
    return False

class Workflow:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions

    @classmethod
    def process_line(cls, line):
        line = line.split('{')
        name = line[0]
        conditions = []

        conds = line[1][:-1].split(',')

        for idx, con in enumerate(conds[:-1]):
            curr = []

            con = con.split(':')

            if con[0][1] == '<':
                curr.extend([con[0][0], [0, int(re.findall(r'(\d+)', con[0])[0])]])
            else:
                curr.extend([con[0][0], int(re.findall(r'(\d+)', con[0])[0])])

            curr.append(con[-1])
            conditions.append(curr)

        conditions.append(conds[-1])

        return cls(name, conditions)

with open('input.txt', 'r') as inp_data:
    data = inp_data.read().split('\n\n')

    workflows = data[0].split('\n')
    workflows_list = {}

    for workflow in workflows:
        to_add = Workflow.process_line(workflow)
        workflows_list[to_add.name] = to_add

    parts = data[1].split('\n')
    parts_list = []

    for part in parts:
        parts_list.append(Part.process_line(part))

    output = 0
    for part in parts_list:
        pointer = 'in'
        while pointer not in ['R', 'A']:
            pointer = part.check_con(workflows_list[pointer].conditions)

        if pointer == 'A':
            output += part.get_sum()

    print(output)