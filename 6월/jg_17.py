import sys
sys.stdin = open('input.txt')

# N = int(input())
N = 3
# K = int(input())
K = 7
# arr1, arr = [[0 for i in range(N+1)] for _ in range(N+1)], []
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         arr.append(i*j)
# arr.sort()

left, right = 1, K

while left <= right:
    mid = (left+right) // 2
    res = 0
    for i in range(1, N+1):
        res += min(mid//i, N)
    if res >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
