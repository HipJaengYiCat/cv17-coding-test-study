# n = 3
# data = ['1212345', '1212356', '0033445']

# n = int(input())
# data = [str(input()) for _ in range(n)]

result = 1
while True:
    num = []
    for s in data:
        num.append(s[-1*result:]) # num에 길이가 result인 번호 넣음

    if len(set(num)) == n: # 고유하게 나오면 끝
        break

    elif len(set(num)) != n: # 중복이 있으면 result + 1
        result+=1

print(result)