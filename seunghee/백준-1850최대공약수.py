from math import gcd # gcd만 가져오긴
n, m = map(int, input().split())
result = '1' * gcd(n, m) # int로 바꿀필요없음 - 시간초과
print(result)