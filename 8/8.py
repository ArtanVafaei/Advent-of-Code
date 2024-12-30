import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

lines = D.split('\n')
ROWS, COLS = len(lines), len(lines[0])
antinodes = set()
antinodes2 = set()
antenna_to_coords = defaultdict(list)
p1 = 0

for r in range(ROWS):
    for c in range(COLS):
        if lines[r][c] != '.':
            antenna_to_coords[lines[r][c]].append((r, c))
            antinodes2.add((r, c))

for coords in antenna_to_coords.values():
    for r1, c1 in coords:
        for r2, c2 in coords:
            if (r1, c1) == (r2, c2):
                continue

            dr, dc = r2 - r1, c2 - c1
            if 0 <= r2 + dr < ROWS and 0 <= c2 + dc < COLS:
                antinodes.add((r2 + dr, c2 + dc))

                while 0 <= r2 + dr < ROWS and 0 <= c2 + dc < COLS:
                    r2 += dr
                    c2 += dc
                    antinodes2.add((r2, c2))

p1 = len(antinodes)
p2 = len(antinodes2)
print(p1)
print(p2)