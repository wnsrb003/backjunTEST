import sys

t = int(sys.stdin.readline())



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
    
arr = sosu(1299709)
for _ in range(t) :
    n = int(sys.stdin.readline().strip())
    if arr[n] : print(0)
    else :
        a = 2
        b = 1299709
        for i in range(n-1,0,-1):
            if arr[i] : 
                a = i
                break
        for i in range(n+1,1299710) :
            if arr[i] : 
                b = i
                break
        print(b-a)

# print(arr[23])
# print(arr[11])
# print(arr[10])