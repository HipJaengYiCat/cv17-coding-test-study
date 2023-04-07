n = int(input())

d = [[0] * 11 for i in range(n+1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10, 0, -1):
        d[i][j] = sum(d[i-1][:j+1])

print(sum(d[n])%10007)