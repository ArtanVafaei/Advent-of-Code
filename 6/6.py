import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

my_map = D.split('\n')
ROWS, COLS = len(my_map), len(my_map[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
visited = set()

def find_starting_position():
    for i in range(ROWS):
        for j in range(COLS):
            if my_map[i][j] == '^':
                return i, j
            
sr, sc = find_starting_position()
r, c = sr, sc
dr, dc = directions[d]

while r >= 0 and r < ROWS and c >= 0 and c < COLS:
    visited.add((r, c))
    nr, nc = r + dr, c + dc

    while nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and my_map[nr][nc] == '#':
        d = (d + 1) % 4
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc

    r, c = nr, nc

p1 = len(visited)
p2 = 0

for o_r in range(ROWS):
    for o_c in range(COLS):
        r, c = sr, sc
        d = 0
        dr, dc = directions[d]
        visited = set()

        while r >= 0 and r < ROWS and c >= 0 and c < COLS:
            if (r, c, d) in visited:
                p2 += 1
                break

            visited.add((r, c, d))
            nr, nc = r + dr, c + dc

            while nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (
                my_map[nr][nc] == '#' or (nr, nc) == (o_r, o_c)
            ):
                d = (d + 1) % 4
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc

            r, c = nr, nc

print(p1)
print(p2)