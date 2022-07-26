num_list = list(range(1, 10001))
delete_list = num_list[:]  # delete_list = num_list로 선언하면 주소가 같아서 동기화됨

for i in num_list :
  if i<10 :
    i = i + i
    delete_list.remove(i)

  elif i<100 :
    i = i + i//10 + i%10
    delete_list.remove(i)

  elif i<1000 :
    i = i + i//100 + (i//10-i//100*10) + i%10
    if i in delete_list :
      delete_list.remove(i)

  else :
    i = i + i//1000 + (i//100-i//1000*10) + (i//10-i//100*10) + i%10
    if i <= 10000 and i in delete_list :
      delete_list.remove(i)


for i in delete_list :
  if i < 100 :
    print(i)