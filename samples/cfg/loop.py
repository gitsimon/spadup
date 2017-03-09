"""
This script does find the ratio gc_count / total_count in dna sequence passed on standard input.
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

total_count: int = 0
gc_count: int = 0

for nucl in nucleotides:
    total_count += 1
    if nucl == 'C' or nucl == 'G':
        gc_count += 1

print(gc_count / total_count)
