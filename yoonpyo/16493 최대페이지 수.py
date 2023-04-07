n,m=map(int,input().split())
bag=[]
for i in range(m):
    day,page=map(int,input().split())
    bag.append((day,page))
bag.sort(key=lambda x:-x[1])

dp=[0]*(n+1)
for day,page in bag:
    for i in range(n,day-1,-1):
        dp[i]=max(dp[i],dp[i-day]+page)
        #dp[i], dp[i-2]+200
        #dp[i], dp[i-4]+40
        #dp[i], dp[i-5]+20
        #dp[i], dp[i-1]+20
        #dp[i], dp[i-2]+15
        #dp[i], dp[i-3]+10
        #dp[i], dp[i-1]+10
    print(dp)


print(dp)


