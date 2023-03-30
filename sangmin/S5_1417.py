'''
9:01
내림차순 정렬
첫 번째 원소 -1 

내림차순


'''


N = int(input())
dasom = int(input())
NumOfVote = [int(input()) for _ in range(N-1)]
count = 0
if len(NumOfVote) == 0:
    print(0)
else:   
    while True:
        NumOfVote.sort(reverse = True)
        if NumOfVote[0] < dasom:
            print(count)
            break
        NumOfVote[0] -= 1
        dasom += 1
        count += 1