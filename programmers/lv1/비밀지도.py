def solution(n, arr1, arr2):
    answer = [''] * n
    for row in range(n):
        password = 0
        for i in range(n):
            if 1 << i & arr1[row] or 1 << i & arr2[row]:
                password += 1 << i
        
        for j in range(n - 1, -1, -1):
            if 1 << j & password:
                answer[row] += '#'
            else:
                answer[row] += ' '
        
    return answer