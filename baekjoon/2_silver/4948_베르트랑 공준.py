def get_prime(max_num):
    array = [True] * (max_num+1)
    for i in range(2, int(max_num**0.5) + 1) :
      if array[i] :
        array[i*2::i] = [False] * (max_num//i - 1)
    return array

array = get_prime(123456*2)
while True :
  n = int(input())
  if n == 0 :
    break
  prime_check = array[n+1:2*n+1]
  print(prime_check.count(True))