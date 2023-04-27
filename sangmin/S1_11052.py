'''
3:00 -> 3:23
배낭 문제처럼 접근하니 금방 풀림
1. 인덱스를 weight-1(리스트의 원소는 0부터 시작이니 -1을 해줌), 원소를 value로 하는 리스트 dp를 생성
2. dp[i] = max(dp[i],dp[i-j-1]+dp[j]) bottom-up 방식을 이용하여 순차적으로 접근하며 업데이트
ex) dp[4] = max(dp[4], dp[3]+dp[1],dp[2]+dp[2])

input
4
1 5 6 7

result
i,j = 0,0
dp = [1,5,6,7] # 초기화

i,j = 1,0
dp[1] = max(dp[1],dp[0]+dp[0])
dp = [1,5,6,7]

i,j = 2,0
dp[2] = max(dp[2],dp[1]+dp[0])
dp = [1,5,6,7]

i,j = 2,1
dp[2] = max(dp[2],dp[0]+dp[1])

i,j = 3,0
dp[3] = max(dp[3],dp[2]+dp[0])
dp = [1,5,6,7]

i,j = 3,1
dp[3] = max(dp[3],dp[1]+dp[1])
dp = [1,5,6,10]


'''



N = int(input())
dp = list(map(int,input().split(" ")))
for i in range(N):
    for j in range(i):
        dp[i] = max(dp[i],dp[i-j-1]+dp[j])
print(dp[-1])
