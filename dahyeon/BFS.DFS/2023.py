n = int(input())

def check2(num):
  for i in range(2, int(num**(1/2))+1):
    if num % i == 0:
      return False
  return True    

def tree(l,r): #현재 자리수와 값
  if l == n: #4자리에 도달할 때까지 진행됐으면
    print(r)
  else :
    for i in range(1,10,2) : #홀수 1,3,5,7,9만 붙이면 됨
      if check2(int(str(r)+str(i))): #뒤에 붙인게 소수면
        tree(l+1, int(str(r)+str(i))) #더 붙이자

lst = [2,3,5,7]
for i in lst:
  tree(1, i)
      