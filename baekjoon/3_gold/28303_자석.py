from sys import stdin

n, k = map(int, stdin.readline().split())
energy = list(map(int, stdin.readline().split()))

ns_dp = [-1e9] * n
sn_dp = [-1e9] * n
for i in range(1, n):
    ns_dp[i] = max(0, ns_dp[i - 1]) + energy[i - 1] - energy[i] - k
    sn_dp[i] = max(0, sn_dp[i - 1]) + energy[i] - energy[i - 1] - k

print(max(max(ns_dp), max(sn_dp)))
