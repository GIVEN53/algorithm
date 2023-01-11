from collections import Counter
from sys import stdin

_ = stdin.readline()
nums = Counter(stdin.readline().split())

_ = stdin.readline()
my_nums = stdin.readline().split()

print(' '.join(f'{nums.get(i, 0)}' for i in my_nums))