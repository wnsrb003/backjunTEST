import sys

n = int (sys.stdin.readline())
def sosu(n) :
    arr = [True] * (n + 1) # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True: # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr
    
arr = sosu(n)

if arr[n] : 
    print(n)
    exit(0)

temp = n
result = []
for i in range(2,n+1) :
    if arr[i] == True :
        while temp % i == 0 :
            result.append(i)
            temp = temp // i
    if temp == 1 : 
        break
for i in result :
    print(i)
# print(result)