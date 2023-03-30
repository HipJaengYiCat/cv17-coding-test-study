from itertools import combinations

n = int(input())

list = [input() for _ in range(n)]

ct = 0
st = 0
for j in range(len(list[0])):
    ct += 1
    list2 = [k[-(j+1):] for k in list] #뒤에서부터 j+1번째까지의 단어를 list2에 담는다.
    for l, m in combinations(list2, 2):
        if l == m:
            st += 1
    if st == 0:
        break
    list2 = []
    st = 0
print(ct)