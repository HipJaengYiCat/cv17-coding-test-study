
## 경우 1: tre??dfs?? 이용
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
      
## 경우 2: 비효율 코드
# import math
# import sys
# input = sys.stdin.readline
# def check(n,a):
#   lst = []
#   cnt = 0
#   for j in range(n):
#     tmp = int(str(a)[:j+1])
#     if len(str(tmp)) >=2 and int(str(tmp)[-1]) % 2 == 0: #뒤에가 짝수면 
#         return False
#     lst.append(tmp)

#   for i in lst:
#     for j in range(2, int(math.sqrt(i))+1):
#       if i % j == 0:
#         return False    
#     cnt += 1  
#   if len(lst) == cnt: #4개 모두 소수면 
#     return True   


# n = int(input())

# lst = [2,3,5,7]
# if n == 1:
#   print(*lst, sep="\n")
# else:  
#   for i in range(2*10**(n-1)+1, 10**(n), 2):
#     if int(str(i)[0]) in lst and check(n,i) == True:
#       print(i)

      