words = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0

for i in words :
  for j in dial :
    if i in j :
      result = result + dial.index(j) + 3

print(result)