import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

topographic_map = D.split("\n")
ROWS, COLS = len(topographic_map), len(topographic_map[0])
p1 = 0

def dfs(r, c, visited):
    if (r, c) in visited:
        return set()
    if topographic_map[r][c] == "9":
        return {(r, c)}

    visited.add((r, c))
    reachable = set()
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < ROWS and 0 <= nc < COLS and
            int(topographic_map[nr][nc]) == int(topographic_map[r][c]) + 1
        ):
            reachable.update(dfs(r + dr, c + dc, visited))
    return reachable

p2 = 0
dp = {}

def dfs2(r, c):
    if (r, c) in dp:
        return dp[(r, c)]
    if topographic_map[r][c] == "9":
        return 1

    dp[(r, c)] = 0
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < ROWS and 0 <= nc < COLS and
            int(topographic_map[nr][nc]) == int(topographic_map[r][c]) + 1
        ):
            dp[(r, c)] += dfs2(r + dr, c + dc)
    return dp[(r, c)]

for r in range(ROWS):
    for c in range(COLS):
        if topographic_map[r][c] == "0":
            reachable_nines = dfs(r, c, set())
            p1 += len(reachable_nines)
            p2 += dfs2(r, c)

print(p1)
print(p2)