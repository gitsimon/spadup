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
x3 = input()  # ANALYSIS SAYS: x3 unused

# {x1, x2}
if x1 <= x2 and x2 <= x2:  # bug
    # {}
    asc = False
    # {asc}
else:
    # {}
    asc = True
    # {asc}

# {asc}
print(asc)
# {}
