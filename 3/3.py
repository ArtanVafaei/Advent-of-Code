import sys
from re import findall

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

p1 = 0
p2 = 0
enabled = True

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", D):
    if do:
        enabled = True
    elif dont:
        enabled = False
    else:
        p1 += int(a) * int(b)
        if enabled:
            p2 += int(a) * int(b)

print(p1)
print(p2)