n,m = map(int, input().split())
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(1,m+1):
  k, page = map(int, input().split())
  for w in range(1,n+1):
    if w-k >= 0:
      dp[i][w] = max(dp[i-1][w], dp[i-1][w-k]+page)
    else:
      dp[i][w] = dp[i-1][w]
# print(*dp,sep="\n")

print(dp[m][n])