from sys import stdin


def dfs(now):
    global max_cnt

    if now == n:  # 마지막까지 계란치기 끝났으면 최댓값 갱신
        cnt = sum(1 for e in eggs if e[0] < 1)
        max_cnt = max(max_cnt, cnt)
        return

    if eggs[now][0] < 1:  # 손에 든 계란이 이미 깨짐
        dfs(now + 1)
        return

    broken = False
    for next in range(n):
        # 손에 든 계란이거나 이미 깨진 다음 계란 건너뛰기
        if now == next or eggs[next][0] < 1:
            continue

        broken = True
        eggs[now][0] -= eggs[next][1]
        eggs[next][0] -= eggs[now][1]
        dfs(now + 1)  # 다음 계랸
        eggs[now][0] += eggs[next][1]
        eggs[next][0] += eggs[now][1]

    if not broken:
        dfs(now + 1)  # 계란치기를 한 번도 못했으면 다음 계란


n = int(stdin.readline())
eggs = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_cnt = 0
dfs(0)

print(max_cnt)
