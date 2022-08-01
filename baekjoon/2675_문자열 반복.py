T = int(input()) # test case

for i in range(T) :
  r, str = input().split()
  r = int(r)
  result = ""
  for i in str :
    result = result + i*r
  print(result)
