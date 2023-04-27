'''
오르막수
길이 N이 주어지면 길이가 N인 증가하는 수열의 개수를 구해라
'''
N = int(input())
srt = 10**(N)//10 if N != 1 else (10**(N)//10-1)
end = 10**(N)
cnt = 0
# for i in range(srt,end):
#     s = str(i)
'''
dp[i][0] = sum(dp[i-1])
dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
'''
dp = [[0]*(10) for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1
temp = sum(dp[1])
for i in range(2,N+1):
    for j in range(10):
        dp[i][j] =  temp
        temp-=dp[i-1][j]
        
    temp = sum(dp[i])
print(sum(dp[-1])%10007)