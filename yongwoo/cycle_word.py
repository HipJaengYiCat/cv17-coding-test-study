from collections import deque

n = int(input())
word_list = []

for _ in range(n):
    linked_list = deque(input())
    for _ in range(len(linked_list)):
        tmp = ''.join(linked_list)
        if tmp in word_list:
            flag = True
            break
        linked_list.rotate()
    else:
        word_list.append(tmp)

print(len(word_list))