import sys
N = int(input())
alphabets_dict = {}

for _ in range(N) :
  alphabets = sys.stdin.readline().rstrip()

  for j in range(len(alphabets)) :
    if alphabets[j] in alphabets_dict :
      alphabets_dict[alphabets[j]] += 10 ** (len(alphabets)-j-1)
    else :
      alphabets_dict[alphabets[j]] = 10 ** (len(alphabets)-j-1)
alphabets_dict = dict(sorted(alphabets_dict.items(), key=lambda x:x[1], reverse=True))

sum, num = 0, 9
for i in alphabets_dict.values() :
  sum += i*num
  num -= 1

print(sum)