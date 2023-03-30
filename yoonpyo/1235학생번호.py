n=int(input())
nlist=[]
for i in range(n):
    nlist.append(int(input()))
k=1
while True:
    newlist=[]
    for i in nlist:
        newlist.append(str(i)[-k:])
    if len(set(newlist))==len(newlist):
        break
    k+=1
print(k)
