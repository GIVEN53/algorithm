str = input().upper() # 대문자로 변환
str_set = set(str) # 중복제거

max_cnt = 0
result = ""
for i in str_set :
  cnt = str.count(i)

  if cnt > max_cnt :
    max_cnt = cnt
    result = i
  elif cnt == max_cnt :
    result = "?"

print(result)