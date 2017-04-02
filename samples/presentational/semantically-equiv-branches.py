"""
This script finds if a list of 3 integers is sorted ascending
"""
import fileinput
from typing import List
xs: List(int)
x = input()  # x unused
a = input()
b = input()

if x <= 0:
    res = a+b
else:
    res = b+a

print(res)
