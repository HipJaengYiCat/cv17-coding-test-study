from collections import deque

n = int(input())
word_list = []
flag = False

for _ in range(n):
    linked_list = deque(input())
    for _ in range(len(linked_list)):
        tmp = ''.join(linked_list)
        if tmp in word_list:
            flag = True
            break
        linked_list.rotate()
    if not flag:
        word_list.append(tmp)
    flag = False

print(len(word_list))