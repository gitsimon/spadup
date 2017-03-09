"""
This script does find the ratio gc_count / total_count in dna sequence passed on standard input.
"""
import fileinput

# Input:
"""
TGGAGTCAGGTATCACCAGTGGTTTCCTGCGATCGACGCG
TGCGGCTGGGCGTATGGAGANGNCCATGGTTCCTTGACGT
GGCGCATTGCGAGAGCTGTCGATGACGTCGCCCGGCTTCA
ATACGGGGAGTGTACCCGACGCGATTGCCCCGCAATCTGG
"""

total_count = 0
gc_count = 0

for line in fileinput.input():
    nucleotides = line.strip()

    for nucl in nucleotides:
        total_count += 1
        if nucl == 'C' or nucl == 'G':
            gc_count += 1

print(gc_count / total_count)
