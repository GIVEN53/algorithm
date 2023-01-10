def check_prime(num) :
  if num == 2 :
    return True
  elif num == 1 or num%2 == 0 : # 1, 짝수 제외
    return False

  for i in range(3, num, 2) : # 홀수만 체크
    if num%i == 0 :
      return False
  return True

M = int(input())
N = int(input())

total = 0;
min = 10001
for i in range(M, N+1) :
  if check_prime(i) :
    total += i
    if i < min :
      min = i
      
if total == 0 :
  print(-1)
else :
  print(total)
  print(min)
