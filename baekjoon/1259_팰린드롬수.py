# 1
def is_palindrome(n):
    mid = len(n)//2
    left = n[:mid]
    if len(n) % 2 == 0:
        right = n[mid:]
    else:
        right = n[mid+1:]

    idx = 0
    while idx < len(left):
        if left[idx] != right[len(right) - idx - 1]:
            return False
        idx += 1
    return True

while 1:
    n = input()
    if n == '0':
        break
    if is_palindrome(n):
        print('yes')
    else:
        print('no')


# 2
while 1:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')