from sys import stdin, setrecursionlimit


def pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    print(root, end=' ')

    root_idx = in_order_idx[root]
    left = root_idx - in_start
    right = in_end - root_idx

    pre_order(in_start, root_idx - 1, post_start, post_start + left - 1)
    pre_order(root_idx + 1, in_end, post_end - right, post_end - 1)


setrecursionlimit(10**6)
n = int(stdin.readline())
in_order = [*map(int, stdin.readline().split())]
post_order = [*map(int, stdin.readline().split())]

in_order_idx = [0] * (n + 1)
for idx, node in enumerate(in_order):
    in_order_idx[node] = idx
pre_order(0, n - 1, 0, n - 1)
