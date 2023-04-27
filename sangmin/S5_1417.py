'''
9:01->9:14

dasom: 다솜의 득표수
count: 다솜이 매수한 사람의 수
NumOfVote: 다솜을 제외한 사람들의 득표수

1. NumOfVote 내림차순 정렬 -> 득표수가 많은 순부터 적은 순으로 정렬
2-1. numofvote의 첫번째 사람이 다솜의 득표수 보다 많으면 첫번째 사람을 투표한 사람 매수
    ->dasom += 1
      count += 1
      NumOfVote -= 1
      1.번 부터 반복
2-2. numofvote의 첫번째 사람이 다솜의 득표수 보다 적으면
-> 다솜 당선 확실-> count를 출력하고 반복문 탈출
    

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