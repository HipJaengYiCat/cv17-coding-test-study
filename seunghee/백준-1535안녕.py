N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

life = 100
score = 0

## 효용버전
data = [(l,j, j-l) for l, j in zip(L, J)] # 손실, 기쁨, 효용
data.sort(key=lambda x : -x[2]) # 효용 큰 순서대로

for thank in data:
    a, b, c= thank
    if life - a > 0:
        life -= a
        score = max(score, score+b)

print(score)  # 반례란.....