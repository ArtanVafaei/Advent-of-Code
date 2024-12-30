import sys

infile = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
D = open(infile).read().strip()

equations = D.split('\n')
p1 = 0
p2 = 0

def is_possible(val, nums, concat=False):
    if len(nums) == 1:
        return val == nums[0]
    res = is_possible(val, [nums[0] + nums[1]] + nums[2:], concat) or \
          is_possible(val, [nums[0] * nums[1]] + nums[2:], concat)
    return res if not concat else \
           res or is_possible(val, [int(str(nums[0]) + str(nums[1]))] + nums[2:], concat)

for equation in equations:
    val, nums = equation.split(':')
    val = int(val)
    nums = list(map(int, nums.split()))
    if is_possible(val, nums):
        p1 += val
    if is_possible(val, nums, concat=True):
        p2 += val

print(p1)
print(p2)