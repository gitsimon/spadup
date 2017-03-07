from functools import reduce
import fileinput

# Input:
"""
Julia	f	153
Beat	m	188
Manuel	m	169
Sabine	f	169
Philip		178
Laura	f	166
"""


def average(data):
    values = data['m'] + data['f']
    return reduce(lambda x, y: x + y, values) / len(values)


if __name__ == "__main__":
    data = {}

    for line in fileinput.input():
        (name, gender, body_height) = line.strip().split('\t')
        if not gender in data:
            data[gender] = []
        data[gender].append(int(body_height))

    print(data)  # {'f': [153, 169, 166], 'm': [188, 169], '': [178]}
    print(average(data))  # 169.0
