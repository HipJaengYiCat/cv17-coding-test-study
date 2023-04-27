from math import gcd
a,b=map(int,input().split())
print("1"*gcd(a,b)) # gcd를 먼저 해줘야함
# 시도1: print("1"*abs(a-b)) - 메모리 초과
# 시도2: x=int("1"*a), y=int("1"*b), gcd(x,y) - 메모리 초과