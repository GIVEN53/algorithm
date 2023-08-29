from sys import stdin
from itertools import combinations


# 1
def get_team_stat(team):
    team_stat = 0
    for member in combinations(team, 2):
        team_stat += s[member[0]][member[1]] + s[member[1]][member[0]]

    return team_stat


n = int(stdin.readline())
s = [list(map(int, stdin.readline().split())) for _ in range(n)]

members = set(range(n))
comb = list(combinations(members, n // 2))
case_cnt = len(comb) // 2
res = 1e9
for start_team in comb:
    if case_cnt == 0:
        break

    case_cnt -= 1
    link_team = tuple(members - set(start_team))
    res = min(res, abs(get_team_stat(start_team) - get_team_stat(link_team)))

print(res)

##########################
#    memory: 56392KB     #
#    time:   1260ms      #
##########################


# 2
n = int(stdin.readline())
s = [list(map(int, stdin.readline().split())) for _ in range(n)]

member_stat = [sum(i) + sum(j) for i, j in zip(s, zip(*s))]
total_stat = sum(member_stat) // 2

res = 1e9
for c in combinations(member_stat[:-1], n // 2):
    res = min(res, abs(total_stat - sum(c)))

print(res)

##########################
#    memory: 31256KB     #
#    time:   96ms        #
##########################
