"""
This script finds if a dna sequence (passed on standard input) starts with a G or C nucleotide.
"""
import fileinput
from typing import List

# Input:
"""
TGGAGTCAGGTATCACCAGTGGTTTCCTGCGATCGACGCG
TGCGGCTGGGCGTATGGAGANGNCCATGGTTCCTTGACGT
GGCGCATTGCGAGAGCTGTCGATGACGTCGCCCGGCTTCA
ATACGGGGAGTGTACCCGACGCGATTGCCCCGCAATCTGG
"""

nucleotides: List[str] = []
for line in fileinput.input():
    nucleotides += line.strip()

first: str = nucleotides[0]

print(first)
