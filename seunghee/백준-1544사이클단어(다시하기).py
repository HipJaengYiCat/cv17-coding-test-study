# 1544 사이클 단어 - 다시풀기

# N = int(input())
# data = [map(str, input().split()) for _ in range(N)]
data = ['picture', 'turepic','icturep','word','ordw']
# data
from collections import deque
N = 5#int(input())
# data = [map(str, input().strip()) for _ in range(N)] #-> deque로

# 단어 하나를 꺼내서 기존 단어와 같으면 정리해서 다시 Insert
for i in range(N):
    word = data[i]
    que =deque(word) # picture -> ['p', 'i', 'c', 't', 'u', 'r', 'e']
    print('시작', data[i], que)

    while True: #-> for로 바꾸기 조건 변경  -> len
        que.append(que.popleft()) # 앞에서 빼서 맨 뒤로 넣기 rotate
        rotate_word = ''.join(que) # 하나씩 밀린 단어
        print(rotate_word)
        if rotate_word == data: #
            print('break')
            break

        if rotate_word in data: # data에 word(하나씩 밀린 단어) 있음 -> 밀린단어를 원래 단어로 변경
            idx = data.index(rotate_word)
            data[idx] = word

        # 중복 단어 없을때 경우

print(len(set(data)))
# return len(set(data))