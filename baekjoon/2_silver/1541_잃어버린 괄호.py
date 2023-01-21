from sys import stdin


expression = list(stdin.readline().rstrip().split('-'))
for i in range(len(expression)):
    expression[i] = sum(map(int, expression[i].split('+')))

ans = expression[0]
for i in range(1, len(expression)):
    ans -= expression[i]
print(ans)
