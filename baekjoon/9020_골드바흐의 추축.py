def is_prime(num) :
  if n == 1 :
    return False

  for i in range(2, int(num**0.5) + 1) :
    if num%i == 0 :
      return False
      
  return True


import sys
T = int(input())
for i in range(T) :
  n = int(sys.stdin.readline())
  num1, num2 = n//2, n//2

  while num1 > 0 :
    if is_prime(num1) and is_prime(num2) :
      print(num1, num2)
      break
    else :
      num1 -= 1
      num2 += 1