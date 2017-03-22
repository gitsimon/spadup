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

x1 = input()  # ANALYSIS SAYS: x1 unused
x2 = input()  # ANALYSIS SAYS: x2 unused
x3 = input()  # ANALYSIS SAYS: x3 unused

# {}
asc = False

# {asc}
"""
x1,x2,x3 are not in set since none of the use-def-chains of any vars in property set anywhere inside if, i.e. {asc}, do not end inside if-stmt
"""
if x1 <= x2 <= x3:
    # {asc}
    temp = False
    # {asc}
else:
    # {asc}
    temp = True
    # {asc}

# {asc}
print(asc)
# {}
asc = temp  # BUG, should be before print
# {}
