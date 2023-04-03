"""
실버 1 : 11057 오르막 수
시작 : 4:00
성공 : 4:23
"""

n = int(input()) #오르막 수 길이
dp = [[1]*10 for _ in range(n+1)] #0~10

for i in range(2,n+1):
  for j in range(10): #0~9
    dp[i][j] = sum(dp[i-1][j:])

# print(*dp, sep = "\n")
print(sum(dp[n])%10007)