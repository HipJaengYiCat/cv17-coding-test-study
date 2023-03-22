n = int(input())
lst = []
cnt = 0 #감소 횟수
for _ in range(n):
  lst.append(int(input())) #입력

for i in range(n-1,0,-1): 
  if lst[i-1] < lst[i]: 
    continue
  else : #감소시켜야하는 경우
    cnt += lst[i-1] - lst[i] + 1
    lst[i-1] = lst[i]-1
  
print(cnt)
    