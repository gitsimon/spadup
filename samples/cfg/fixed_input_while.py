"""
This script finds the number of divisors of input x.
"""
import fileinput
from typing import List

# Input:
"""
12
"""

x = int(input()) # ANALYSIS SAYS: x used (but is not)
# {x}
count = 1
# {count (pct: 1 > x || x%1 != 0), x}
i = 2
# {count (pct: i > x || x%i != 0), i, x}
while i <= x:
    # {count (pct: x%i != 0)}
    if x % i == 0:
        # {}
        count = 1  # BUG, should be: count += 1
        # {count}
    # {count}
    i += 1
    # {count}

# {count}
print(f"Integer has {count} divisors")
# {}