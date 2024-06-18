# 1 (1820 ms)
from sys import stdin


def compare(a, b):
    if a == b:
        return "good puzzle"

    b = [-x for x in b]
    b.sort()
    if a == b:
        return "good puzzle"
    return "bad puzzle"


n = int(stdin.readline())
puzzle = list(map(int, stdin.readline().split()))
other = list(map(int, stdin.readline().split()))

puzzle_diff = [puzzle[i] - puzzle[(i + 1) % n] for i in range(n)]
puzzle_diff.sort()
other_diff = [other[i] - other[(i + 1) % n] for i in range(n)]
other_diff.sort()

print(compare(puzzle_diff, other_diff))


# 2 (380 ms)
from sys import stdin

n = int(stdin.readline())
puzzle = stdin.readline().split()
other = stdin.readline().split()

p = other.index(puzzle[0])
if puzzle in [other[p:] + other[:p], other[p::-1] + other[:p:-1]]:
    print("good puzzle")
else:
    print("bad puzzle")
