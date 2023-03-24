'''
백준 브론즈 3
'''
k = int(input())
input_list = [list(map(int,input().split(" "))) for _ in range(k)]


for H,W,N in input_list:
    if N % H != 0: 
        floor = N%H #층
        room_num = N//H+1#호수
    else:# 사람의 수와 호텔 층수의 나머지가 0 -> 꼭대기 층에 배정되었다는 의미
        floor = H
        room_num = N//H
    print(str(floor)+str(room_num).zfill(2)) #w 가 2자리가 최대라서 2자리까지 0으로 채웠다
                