def hansu(num) :
  cnt = 0
  if num < 100 :
    return num

  elif num >= 100 :
    for i in range(100, num+1) :
      ap1 = int(str(i)[0]) - int(str(i)[1])
      ap2 = int(str(i)[1]) - int(str(i)[2])
      if ap1==ap2 :
        cnt +=1
    cnt += 99
    return cnt
      


num = hansu(int(input()))

print(num)

# import sys
# input = sys.stdin.readline
# def han(x):
#     a = 0
#     for i in range((n//100)*100, x+1):
#         i = list(map(int,str(i)))
#         if i[0] - i[1] == i[1] - i[2]:
#             a += 1
#     return a
    
# n = int(input()) 
# cnt = 0
# if n <= 99:  
#     print(n)
# else:
#     if n // 100 >= 2:
#         cnt += ((n // 100)-1)*5
#         cnt += han(n)
#     else:   
#         cnt += han(n)
#     print(cnt+99)