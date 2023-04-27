"""
문제 : 4358 실버2 생태학

round 쓰지 말기
"""

import sys
input = sys.stdin.readline
dic = {}
cnt = 0
while 1:
  a = input().rstrip()
  if a == "":
    break
  cnt += 1  
  if a not in dic.keys():
    dic[a] = 1
  else:
    dic[a] +=1

sorted_k = sorted(dic.items())


for k,v in sorted_k:
   print(f'{k} {v/cnt*100:.4f}')

