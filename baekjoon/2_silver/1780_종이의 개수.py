from sys import stdin


def cut(x, y, n):
    if n == 1:
        if paper[x][y] == -1:
            return [1, 0, 0]
        elif paper[x][y] == 0:
            return [0, 1, 0]
        else:
            return [0, 0, 1]

    paper_cnt = [0, 0, 0]
    for i in range(x, x + n, n//3):
        for j in range(y, y + n, n//3):
            paper_cnt = [a + b for a, b in zip(paper_cnt, cut(i, j, n//3))]

    for i in range(3):
        if sum(paper_cnt) == 9 and paper_cnt[i] == 9:
            paper_cnt[i] = 1

    return paper_cnt


n = int(stdin.readline())
paper = [[*map(int, stdin.readline().split())] for _ in range(n)]

print('\n'.join(map(str, cut(0, 0, n))))
