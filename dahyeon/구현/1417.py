"""
문제 : 실버 5 1417 국회의원 선거
시작 : 9:00
성공 : 9:27

다솜이는 1번
2~n 사람들을 매수하면 됨
정렬 후 매수..?
===> 빼준다음 다시 정렬해야한다 !!!!!!!!!!
"""
n = int(input())
lst = []
cnt = 0
for _ in range(n):
  lst.append(int(input()))

da = lst[0]

if n == 1:
  print(0)

else :  
  lst.pop(0) #다솜이를 빼줌
  lst.sort(reverse = True) #내림차순
  
  while 1:
    if da > lst[0] : #다른 사람들보다 다솜이가 크다면
      break
    else:  
      da += 1
      lst[0] -= 1
      cnt += 1
      lst.sort(reverse = True)
  print(cnt)

