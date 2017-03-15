"""
This script finds if a list of 3 integers is sorted ascending
"""
import fileinput
from typing import List

# Input:
"""
1
4
2
"""

x1 = input()
x2 = input()
x3 = input()  # unused

xs = [x1, x2, x3]

asc = True
for i in range(0, 1):  # bug
    asc = asc and xs[i] < xs[i + 1]

print(asc)
