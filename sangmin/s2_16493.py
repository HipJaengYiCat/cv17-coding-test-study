'''
7 7

3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''



N,K = list(map(int,input().split()))
dp = [[0]*(N+1) for _ in range(K+1)]#물건의 개수를 행, 남은 기간을 열

info = [list(map(int,input().split())) for _ in range(K)]
info = [[0,0]]+info



for i in range(1,K+1):#k번째 도서
    for j in range(1,N+1):#N일
        
        if j >= info[i][0]:#만약 i번째 도서를 j일 안에 읽을 수 있다면
            dp[i][j] = max(dp[i-1][j-info[i][0]] + info[i][1],dp[i-1][j])#
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[K][N])

