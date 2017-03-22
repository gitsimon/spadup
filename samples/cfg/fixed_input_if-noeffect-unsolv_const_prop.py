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

# {x1,x2}
asc = True

# {asc, x1, x2}
"""
x1,x2 are in set since the use-def-chains of temp ends inside if-stmt
"""
if x1 <= x2:
    # {asc}
    temp = False
    # {asc, temp}
else:
    # {asc}
    temp = True
    # {asc, temp}

# {asc, temp}
asc = asc and temp

# {asc}
"""
x2,x3 are not in set since none of the use-def-chains of any vars in property set anywhere inside if, i.e. {asc}, do not end inside if-stmt
"""
if x2 <= x3:
    # {asc}
    temp = False
    # {asc}
else:
    # {asc}
    temp = True
    # {asc:53}

# BUG, missing update on asc

# {asc}
print(asc)
# {}
