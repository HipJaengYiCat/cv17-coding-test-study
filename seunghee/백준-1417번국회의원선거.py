N = 3 # 후보 
data = [5,7,7] # 유권자

# N = 4 # 후보
# data = [10,10,10,10] # 유권자

# N = 1 # 후보
# data = [1] # 유권자

# N = 5 # 후보
# data = [5, 10, 7, 3, 8] # 유권자


N = int(input())
data = [int(input()) for _ in range(N)]
## 코드 시작
result = 0

if len(data)  > 1 :
    one = data[0] # 매수자놈 득표수
    others = data[1:] # 나머지 득표수

    while max(others) >= one: # 1번보다 나머지 중 하나가 더 크거나 같으면 -> 가장득표수많은 놈부터 한명씩 매수
        one +=1
        max_idx = others.index(max(others))
        others[max_idx] -= 1
        result += 1 # 매수한놈들 count

else:
    pass
print(result)
# 44초