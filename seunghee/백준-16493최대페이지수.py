N, M = map(int,input().split())
dp = [[0 for x in range(N+1)] for y in range(M+1)]

for i in range(1, M+1): # 챕터 한개씩 탐색
    day, page = map(int, input().split())# ex (3, 10)
    for j in range(1, N+1): # 날짜
        if j >= day : # 읽을 날짜 충분
            dp[i][j] = max(dp[i-1][j], page + dp[i-1][j-day])
            #              바로윗칸    현재 책+남은 기간에 가능한 챕터의 page      
        else : # 읽을 날짜 없음
            dp[i][j] = dp[i-1][j]# 바로 윗칸 -> 같은 날짜(j) 주어질때 읽을 수 있는 수

print(dp[M][N])