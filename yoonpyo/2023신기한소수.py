from math import sqrt
import sys
n=int(sys.stdin.readline())
if n==1:
    print(2)
    print(3)
    print(5)
    print(7)
    exit()
def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def search(n):
    for i in range(10**(n-1)+1,10**n,2):
        #시간 초과
        # num=i
        # for j in range(n):
        #     if num==1 or isprime(num)==False:
        #         break                
        #     elif isprime(num)==True:
        #         pass
        #     num=num//10
        for j in range(1,n+1):
            num=int(str(i)[:j])
            if num==1 or isprime(num)==False:
                break                
            elif isprime(num)==True:
                pass
        else:
            print(i)
search(n)
