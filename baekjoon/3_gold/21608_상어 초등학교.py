from sys import stdin


def sit(my_favorite):
    now_r, now_c = -1, -1
    max_my_favorite_cnt, max_blank_cnt = 0, 0
    for r in range(n):
        for c in range(n):
            if classroom[r][c] != 0:
                continue

            my_favorite_cnt, blank_cnt = 0, 0
            for i in range(4):
                nr, nc = r + direction[i], c + direction[3 - i]
                if is_out_of_range(nr, nc):
                    continue

                if classroom[nr][nc] in my_favorite:
                    my_favorite_cnt += 1
                elif classroom[nr][nc] == 0:
                    blank_cnt += 1

            if my_favorite_cnt > max_my_favorite_cnt:
                max_my_favorite_cnt = my_favorite_cnt
                max_blank_cnt = blank_cnt
                now_r = r
                now_c = c
            elif my_favorite_cnt == max_my_favorite_cnt and blank_cnt > max_blank_cnt:
                max_blank_cnt = blank_cnt
                now_r = r
                now_c = c
            elif now_r == now_c == -1:
                now_r = r
                now_c = c

    return now_r, now_c


def is_out_of_range(r, c):
    return 0 > r or r >= n or 0 > c or c >= n


n = int(stdin.readline())
students = []
my_favorites = [None] * (n**2 + 1)
for _ in range(n**2):
    s, *favorite_students = map(int, stdin.readline().split())
    students.append(s)
    my_favorites[s] = favorite_students

classroom = [[0] * n for _ in range(n)]
direction = [1, 0, -1, 0]
for s in students:
    r, c = sit(my_favorites[s])
    classroom[r][c] = s

satisfaction = 0
for r in range(n):
    for c in range(n):
        s = classroom[r][c]
        favorite_cnt = 0
        for i in range(4):
            nr, nc = r + direction[i], c + direction[3 - i]
            if is_out_of_range(nr, nc):
                continue
            if classroom[nr][nc] in my_favorites[s]:
                favorite_cnt += 1

        if favorite_cnt > 0:
            satisfaction += 10 ** (favorite_cnt - 1)

print(satisfaction)

##########################
#    memory: 31388KB     #
#    time:   164ms        #
##########################
