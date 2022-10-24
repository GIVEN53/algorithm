import math


def check_prime(num) :
  if num == 2 :
    return True
  elif num == 1 or num%2 == 0 : # 1, 짝수 제외
    return False

  for i in range(3, int(math.sqrt(num)) + 1, 2) : # 홀수만 체크
    if num%i == 0 :
      return False
  return True


m, n = map(int, input().split())

for i in range(m, n+1) :
  if check_prime(i) :
    print(i)
