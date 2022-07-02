import sys
sys.stdin = open('input.txt')

# def dfs(index):
#     global result
#     if index >= len(nums):
#         return
#     if sum(r) + nums[index] > M:
#         return
#     r.append(nums[index])
#     result = result if M - result < M - sum(r) else sum(r)
#     for i in range(index+1, len(nums)):
#         dfs(i)
#     r.pop()

I, M = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
# r = []
# dfs(0)
# print(result)
from itertools import permutations
for num in permutations(nums, 3):
    if sum(num) > M:
        continue
    result = result if M - result < M - sum(num) else sum(num)
print(result)