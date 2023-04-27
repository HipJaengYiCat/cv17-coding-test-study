import sys
from collections import deque
n=int(sys.stdin.readline())
wlist=[]
for i in range(n):
    word=sys.stdin.readline().rstrip()
    wlist.append(word)

for i in range(n):
    w=deque(wlist[i])
    while True:
        a=w.popleft()
        w.append(a)
        if ''.join(w)==wlist[i]: # 한바퀴 돌아서 다시 그 단어 되면 break
            break
        if ''.join(w) in wlist: #이미 리스트에 있으면
            wlist.remove(''.join(w))
            wlist.append(wlist[i])
print(len(set(wlist)))
