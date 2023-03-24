case = int(input())

for _ in range(case):
  h,w,n = map(int,input().split()) #층 수, 방 수, 몇 번째 손님
  a,b = [0,0] #객실 위치
  ### 층(h)만큼 나눠서 
  b = n//h+1
  a = n%h
  ## 반례 (1,3)에 3번째 손님 => 정답 : 103 내 코드 : 004
  if a == 0: #각 층의 끝방인 경우. 다음 열로 넘어가면 안됨
    b = n//h
    a = h
  print(str(a)+str(b).zfill(2))


"""
3
6 12 10
30 50 72
1 3 3

"""