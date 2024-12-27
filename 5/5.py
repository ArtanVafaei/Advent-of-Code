import sys
from functools import cmp_to_key

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

rules, updates = D.split('\n\n')
rule_set = set()
p1 = 0
p2 = 0

for rule in rules.split('\n'):
    x, y = rule.split('|')
    rule_set.add((x, y))

cmp = cmp_to_key(lambda x, y: 1 if (x, y) not in rule_set else -1)

for update in updates.split('\n'):
    pages = update.split(',')
    sorted_pages = sorted(pages, key=cmp)
    if pages == sorted_pages:
        p1 += int(pages[len(pages) // 2])
    else:
        p2 += int(sorted_pages[len(sorted_pages) // 2])

print(p1)
print(p2)