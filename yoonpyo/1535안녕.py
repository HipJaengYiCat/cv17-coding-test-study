n=int(input())
h=[]
health=list(map(int,input().split()))
happy=list(map(int,input().split()))
for i in range(n):
    h.append((health[i],happy[i]))
h.sort(key=lambda x:-x[1]) # happy 높은 순으로 정렬
# (21,30),(79,25),(1,20)
dp=[0]*101
for health, happy in h:
    for i in range(100,health-1,-1): #100부터 health까지
            dp[i] = max(dp[i], dp[i-health]+happy)
            #i=100~21  dp[i]와 dp[i-21]+30 중 최대값
            #i=100~79  dp[i]와 dp[i-79]+25 중 최대값
            #i=100~1   dp[i]와 dp[i-1]+20 중 최대값
print(dp[99])