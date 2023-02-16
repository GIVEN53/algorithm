from math import log2


def dfs(bin):
    if len(bin) == 1:
        return 1

    root = len(bin) // 2
    if bin[root] == '0':
        if not all(child == '0' for child in bin):
            return 0

    left = dfs(bin[:root])
    right = dfs(bin[root + 1:])

    return left and right


def get_binary(num):
    bin_num = bin(num)[2:]
    height = int(log2(len(bin_num))) + 1
    tree_len = 2 ** height - 1
    return '0' * (tree_len - len(bin_num)) + bin_num


def solution(numbers):
    answer = []
    for num in numbers:
        bin = get_binary(num)
        answer.append(dfs(bin))

    return answer
