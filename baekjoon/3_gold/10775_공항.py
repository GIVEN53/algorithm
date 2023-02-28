from sys import stdin


def find(x):
    if gate[x] == x:
        return x
    gate[x] = find(gate[x])
    return gate[x]


g = int(stdin.readline())
planes = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
gate = [i for i in range(g + 1)]

cnt = 0
for plane in planes:
    gate_num = find(plane)
    if gate_num == 0:
        break
    gate[gate_num] = gate[gate_num - 1]
    cnt += 1

print(cnt)
