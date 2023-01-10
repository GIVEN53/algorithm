from sys import stdin

def perm(r, num):
    global min_result, max_result

    if r == N+1:
        if int(min_result) > int(num):
            min_result = num
        if int(max_result) < int(num):
            max_result = num
        return

    for i in range(10):
        if not visited[i]:
            if r == 0 or check_inequality_sign(signs[r-1], int(num[-1]), i):
                visited[i] = True
                perm(r+1, num+str(i))
                visited[i] = False

def check_inequality_sign(sign, num1, num2):
    if sign == '>':
        return num1 > num2
    else:
        return num1 < num2

N = int(stdin.readline())
signs = stdin.readline().split()

visited = [False]*10
min_result = "9876543211"
max_result = "0"
perm(0, '')

print(max_result)
print(min_result)
