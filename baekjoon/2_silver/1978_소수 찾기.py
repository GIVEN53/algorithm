def check_prime(num) :
  if num == 2 :
    return True
  elif num == 1 or num%2 == 0 : # 1, 짝수 제외
    return False

  for i in range(3, num, 2) : # 홀수만 체크
    if num%i == 0 :
      return False
  return True


n = int(input())
num_list = list(map(int, input().split()))
cnt = 0;

for i in num_list :
  if check_prime(i) :
    cnt += 1

print(cnt)