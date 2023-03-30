n=int(input())
nlist=[]
dasom=int(input())
for i in range(n-1):
    nlist.append(int(input()))
count=0
if n==1: #사람이 한명이면 가져올 표가 없음
    print(0) # 0 출력
else: #사람이 여러명이면
    while True:
        if max(nlist)<dasom:
            break
        else:
            idx=nlist.index(max(nlist))
            nlist[idx]-=1 # 제일 표많은 사람꺼 하나 뺏어옴
            dasom+=1 # 다솜이 표에 더함
            count+=1
    print(count)
#5 10 7 3 8
#6 9 7 3 8
#7 8 7 3 8
#8 7 7 3 8
    
