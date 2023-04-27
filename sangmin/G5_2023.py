'''
입력 N이 들어왔을때

N의 자리 신기한 수소 모두 출력
신기한소수: 1,2,3,4,5...N의 자리가 모두 소수인 수
'''
import math

N = int(input())

def prime(num):
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
pL = [[] for _ in  range(N)]
pL[0] = [i for i in range(2,10) if prime(i)]
if N==1: #N이 1일때 예외처리
    for a in pL[0]:
        print(a)
    exit()


for i in range(N):
    for num in pL[i]:
        for j in [1,3,5,7,9]:
            temp = num*10 + j
            if prime(temp):
                if len(str(temp))==N:
                    print(temp)
                else:
                    pL[i+1].append(temp)






