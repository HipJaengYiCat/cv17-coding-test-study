'''
9:59->10:10(75% 실패)
10:20 -> 길이가 1일 때 예외 처리
10:24 -> 첫번째 for 문 수정-> 통과
'''
N = int(input())


student_id = [input()[::-1] for _ in range(N)]# 반복문에서 뒷자리 부터 쉽게 탐색하기 위해 문자를 뒤집어서 입력

length = len(student_id[0])

# 10:24-> 수정,마지막 자리까지 탐색하게 코드 수정 
for i in range(length+1): # 10:24 수정사항: for i in range(length) ->for i in range(length+1)
    dict = {}
    for id in student_id: # 
        dict[id[:i]] = 1 # 문자열의 범위를 한글자씩 늘리면서 중복 검사하기 위해 딕셔너리에 넣어줌
    
    if len(dict) == N:  #만약 중복되지않으면 글자수를 출력하고 반복문 종료
      print(i)
      break

if length == 1: #길이가 1일 때 예외
   print(1)