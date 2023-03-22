t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    #세로로 쌓는 느낌
    # h=6 w=12, n=10일때 n//h=1 n%h=4 -> 402
    # h=6 w=12 n=6 일때 n//h=1 n%h=0 -> 601
    # n%h -> 층, (n//h)+1 -> 호수
    if n%h!=0:
        answer=(n%h)*100+((n//h)+1)
    else:
        answer=h*100+(n//h)
    print(answer)

