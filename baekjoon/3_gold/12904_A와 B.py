from sys import stdin

s, t = list(stdin.readline().rstrip()), list(stdin.readline().rstrip())

while len(s) < len(t):
    last = t.pop()
    if last == 'B':
        t = t[::-1]

print(1 if s == t else 0)
