"""
시작 : 4:06
success : 4:24

총평 : 코드가 안 이쁘다
"""
n = int(input())
lst = []
stack = [] #비교를 위한 스택
cnt = 0 #서로 같은 개수 (ans = n - cnt)
for _ in range(n):
  lst.append(input())

for i in range(n-1):
  lst[i] = list(lst[i])
  for j in range(len(lst[i])):
    lst[i].append(lst[i].pop(0))
    if "".join(lst[i]) in lst[i+1:]: #idx 기준 다음 리스트 모든 값과 비교
    #   print("".join(lst[i]), lst[i+1])
      cnt += 1
      break

print(n-cnt)
