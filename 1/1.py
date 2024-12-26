import sys
from collections import Counter

infile = sys.argv[1] if len(sys.argv) >= 2 else '1.in'
D = open(infile).read().strip()

lines = D.split('\n')
left, right = [], []

for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

p1 = 0
for l, r in zip(sorted(left), sorted(right)):
    p1 += abs(l - r)
print(p1)

p2 = 0
right_count = Counter(right)
for n in left:
    p2 += n * right_count[n]
print(p2)