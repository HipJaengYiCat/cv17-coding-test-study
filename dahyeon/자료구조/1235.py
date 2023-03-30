"""
문제 : 1235 실버 4 학생번호
시작 : 9:58
"""

n = int(input())
lst = []
for i in range(n):
  lst.append(input())
l = len(lst[0]) #문자열의 길이
t = False


t = False
for i in range(l-1,-1,-1): #문자열 길이만큼 6~0
  stack = [] #스택 초기화
  cnt = 1 # 다른 수 갯수
  for j in range(n): 
    if j == 0:
      stack.append(lst[j][i:])
      continue
    if lst[j][i:] in stack: #스택에 존재하면
      break
    else :
      cnt += 1
      stack.append(lst[j][i:]) #다른 수 추가
  if cnt == n: #n개 문자를 다 확인했을 때,
    t = True
    print(l-i)
    break
if not t:
  print(0)
"""
3
1212345
1212356
0033445

"""
