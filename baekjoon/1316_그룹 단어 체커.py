def check() :
  word = input()
  word_set = set(word)

  for i in word_set :
    idx_list = []

    for j, value in enumerate(word) :
      if i == value :
        idx_list.append(j) # 문자열의 인덱스 추가
    if len(idx_list) == 1 : # 문자열이 한 개면 1 리턴
      continue;

    for k in range(len(idx_list)-1) : # 인덱스의 차이가 1보다 크면 0 리턴
      if abs(idx_list[k] - idx_list[k+1]) > 1 : # 문자열이 연속적이지 않다는 의미
        return 0 
  return 1

n = int(input())
cnt = 0
for i in range(n) :
  cnt += check()

print(cnt)


# 다른 풀이
"""
n = int(input())
cnt = n

for i in range(n) :
  word = input()
  for j in range(len(word)-1) :
    if word[i] == word[i+1] : # 문자열이 연속적일 때
      pass
    elif word[i] in word[i+1:] : # 연속적이지 않고 이후 문자열에 포함될 때 -1 (해당 단어 제외)
      cnt -= 1
      break

print(cnt)
"""