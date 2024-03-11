import sys
from src.cidrs import CIDRs

c = []
for l in sys.stdin:
    c.append(l.strip())

cidrs = CIDRs(c)
if cidrs.get_errors:
    print('\nInput Warnings:')
    [print(s) for s in cidrs.get_errors()]

# print('\nInput CIDRs:')
# [print(s) for s in cidrs.get_cidrs()]

print('\nSummarized CIDRs:')
[print(s) for s in cidrs.summarize_cidrs()]