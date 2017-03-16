"""
This script finds the number of divisors of x.
"""
import fileinput
from typing import List

# Input:
"""
12
"""

x = int(input())

count = 0
i = 1
while i <= x:  # bug
    if x % i == 0:
        count += 1
    i += 1

print(f"Integer {x} has {count} divisors")
