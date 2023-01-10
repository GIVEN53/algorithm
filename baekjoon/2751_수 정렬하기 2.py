from sys import stdin

nums = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
nums.sort()

print("\n".join(map(str, nums)))
