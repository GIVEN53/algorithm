from sys import stdin

n = int(stdin.readline())
u = sorted([int(stdin.readline()) for _ in range(n)])

tot = set()  # 두 수를 더한 집합
for i in range(n - 1):  # 집합 u에서 가장 큰 수는 더해도 의미없으므로 제외
    for j in range(i, n - 1):
        tot.add(u[i] + u[j])

flag = False
for i in range(n - 1, 0, -1):  # 집합 u에서 가장 큰 수부터 순회
    for j in range(i - 1, -1, -1):
        if u[i] - u[j] in tot:  # 두 수의 차가 두 수를 더한 집합에 포함되면 출력
            print(u[i])
            flag = True
            break
    if flag:
        break
