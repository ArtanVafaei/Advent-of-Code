import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

digits = [int(digit) for digit in D]
blocks = []
id_number = 0
idx = 0
id_to_idx_length = {}

for i, length in enumerate(digits):
    if not i & 1:
        blocks.extend([id_number] * length)
        id_to_idx_length[id_number] = (idx, length)
        id_number += 1
    else:
        blocks.extend(["."] * length)
    idx += length

l, r = 0, len(blocks) - 1
blocks2 = blocks[:]

while l < r:
    if blocks[l] != ".":
        l += 1
        continue
    if blocks[r] == ".":
        r -= 1
        continue

    blocks[l], blocks[r] = blocks[r], blocks[l]
    l += 1
    r -= 1

p1 = 0

for i, id_number in enumerate(blocks):
    if id_number == ".":
        break
    p1 += i * id_number

for id_number in sorted(id_to_idx_length.keys(), reverse=True):
    l = 0
    while l < id_to_idx_length[id_number][0]:
        if blocks2[l] != ".":
            l += 1
            continue

        idx, length = id_to_idx_length[id_number]
        r = l + 1

        while blocks2[r] == ".":
            r += 1

        if length <= r - l:
            blocks2[l:l + length] = [id_number] * length
            blocks2[idx:idx + length] = ["."] * length
            break

        l += 1
        r -= 1

p2 = 0

for i, id_number in enumerate(blocks2):
    if id_number != ".":
        p2 += i * id_number

print("".join(str(x) for x in blocks))
print(p1)
print("".join(str(x) for x in blocks2))
print(p2)