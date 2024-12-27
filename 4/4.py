import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

word_search = D.split('\n')
R = len(word_search)
C = len(word_search[0])
chars = ["X", "M", "A", "S"]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
p1 = 0
p2 = 0

def find_xmas(r, c, dr, dc):
    positions = [
        (r, c),
        (r + dr, c + dc),
        (r + 2 * dr, c + 2 * dc),
        (r + 3 * dr, c + 3 * dc)
    ]
    for i in range(4):
        r, c = positions[i]
        if not (
            r >= 0 and r < R and
            c >= 0 and c < C and
            word_search[r][c] == chars[i]
        ):
            return False
    return True

def find_x_mas(r, c):
    if (r == 0 or r == R - 1 or c == 0 or c == C - 1):
        return False
    return (
        (word_search[r - 1][c - 1] == "M" and word_search[r + 1][c + 1] == "S") or
        (word_search[r + 1][c + 1] == "M" and word_search[r - 1][c - 1] == "S")
    ) and (
        (word_search[r - 1][c + 1] == "M" and word_search[r + 1][c - 1] == "S") or
        (word_search[r + 1][c - 1] == "M" and word_search[r - 1][c + 1] == "S")
    )
    

for r in range(R):
    for c in range(C):
        for dr, dc in directions:
            if find_xmas(r, c, dr, dc):
                p1 += 1
        if word_search[r][c] == "A" and find_x_mas(r, c):
            p2 += 1

print(p1)
print(p2)