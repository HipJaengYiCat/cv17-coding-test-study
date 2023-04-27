'''
4:07-> 4:32
'''
from collections import deque
N = int(input())
cycle_ward = [deque(input()) for _ in range(N)]

dcount = 0 # 같은 단어의 개수
i = 0

while i < N: #인덱스를 유동적으로 바꿀 일이 생길 것 같아 while로 했지만, 다풀고 보니 for문을 사용해도 됨
    for j in range(i+1,N):
        flag = False # i번 째 단어와 같은 단어가 있는지 여부 중복인 단어가 있으면 True
        if len(cycle_ward[i]) != len(cycle_ward[j]):
            continue
        for k in range(len(cycle_ward[i])):
            if cycle_ward[i] == cycle_ward[j]:
                dcount += 1
                flag = True
                break
            else:
                tmp = cycle_ward[j].popleft()
                cycle_ward[j].append(tmp)
        if flag: # i 번째 단어와 같은 단어가 있다면 다음 반복문 종료, 만약 반복문을 종료하지 않으면 같은 단어를 중복해서 카운트함 
            break
    i += 1
print(N-dcount) # 최종 출력은 총단어의 개수 - 중복인 단어