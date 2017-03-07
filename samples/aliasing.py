from functools import reduce
import fileinput

# Input:
"""
1	32	83
48	1	60
23	34	1
"""


def diagonal_sum(matrix):
    sum = 0
    for i in range(0, len(matrix)):
        sum += matrix[i][i]
    return sum


if __name__ == "__main__":
    matrix = []

    row = []
    for line in fileinput.input():
        for val in line.strip().split('\t'):
            row.append(int(val))
        matrix.append(row)

    print(matrix)
    # [[1, 32, 83, 48, 1, 60, 23, 34, 1], [1, 32, 83, 48, 1, 60, 23, 34, 1], [1, 32, 83, 48, 1, 60, 23, 34, 1]]

    print(diagonal_sum(matrix))
    # 116 (instead of 3)
