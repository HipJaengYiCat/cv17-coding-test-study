import math

def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def allp(a):
    start = 10**(a-1) + 1
    end = 10**a
    for i in range(start,end,2):
        for j in range(1,a+1):
            na = int(str(i)[:j])
            if isprime(na):
                pass
            else:
                break
        else:
            print(i)

a = int(input())
if a == 1:
    print(2)
    print(3)
    print(5)
    print(7)
    exit()
allp(a)