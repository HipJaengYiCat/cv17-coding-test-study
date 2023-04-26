import sys
n,m=map(int,sys.stdin.readline().split())
states=[]
limits=[]
def binary_search(limits,target,start,end):
    res=0
    while start<=end:
        mid=(start+end)//2
        if target<=limits[mid]:
            end=mid-1
            res=mid
        else:
            start=mid+1
    return states[res]

for i in range(n):
    state,limit=map(str,sys.stdin.readline().split())
    states.append(state)
    limits.append(int(limit))

for i in range(m):
    power=int(sys.stdin.readline())
    result=binary_search(limits,power,0,n-1)
    print(result)

    

