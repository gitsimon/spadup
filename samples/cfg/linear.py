"""
This script finds if a dna sequence (passed on standard input) starts with a G or C nucleotide.
"""
import fileinput

# Input:
"""
TGGAGTCAGGTATCACCAGTGGTTTCCTGCGATCGACGCG
"""

total_count = 0
gc_count = 0

line = fileinput.input()[0]
nucleotides = line.strip()

first = nucleotides[0]

print(first)
