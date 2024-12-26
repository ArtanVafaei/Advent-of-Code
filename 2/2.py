import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else '1.in'
D = open(infile).read().strip()

def is_safe(report):
    inc = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}

lines = D.split('\n')
p1 = 0
p2 = 0

for line in lines:
    report = list(map(int, line.split()))
    if is_safe(report):
        p1 += 1
    if any([is_safe(report[:i] + report[i + 1:]) for i in range(len(report))]):
        p2 += 1

print(p1)
print(p2)