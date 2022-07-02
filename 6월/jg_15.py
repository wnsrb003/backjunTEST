import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, sum(arr)
c = 0
if N == 1:
    print(arr[0])
    exit(0)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    result = 0
    i = 0
    if max(arr) > mid :
        left = mid + 1
        continue
    while i <= len(arr):
        result += arr[i]
        if i == len(arr) - 1:
            cnt += 1
            result = 0
            break
        if i+1 < len(arr) and result + arr[i+1] > mid:
            cnt += 1
            result = 0
        i+=1
    if cnt < M:
        right = mid - 1
        c = mid
    elif cnt > M:
        left = mid + 1
    elif cnt == M:
        c = mid
        right = mid - 1
    
print(c)
