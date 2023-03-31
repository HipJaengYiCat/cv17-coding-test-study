from itertools import combinations

n = int(input())
h = list(map(int,input().split()))
p = list(map(int,input().split()))

mx = 0
for i in range(1,n+1):
    for j, k in zip(combinations(p,i), combinations(h,i)):
        s = sum([_ for _ in j]) #기쁨
        s2 = sum([_ for _ in k]) #체력
        if s2 < 100:
            mx = max(mx, s)

print(mx)