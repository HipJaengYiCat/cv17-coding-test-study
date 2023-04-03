n = 3#int(input())
dp = [1]*10 # 9~0 순서로 그다음 뒷자리 count  -> 수는 0으로 시작할 수 있다.
# print('시작', dp)
for i in range(1,n) : # 1자리 수부터 n-1자리수 까지 count
    # print(i,'자리수 완료', dp)
    for j in range(1,10) :
        dp[j] += dp[j-1] 
# print(n,'자리수', dp)
print(sum(dp)%10007)