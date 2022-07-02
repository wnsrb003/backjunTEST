import sys
sys.stdin = open('input.txt')
def dfs(index, nums, arr):
    if index >= len(nums):
        return
    arr.append(nums[index])
    if len(arr) == 6:
        print(*arr)
        return
    visited[index] = True
    for i in range(index+1, len(nums)):
        if not visited[i]:
            dfs(i, nums, arr)
            visited[i] = 0
            arr.pop()
            


while(True):
    n = list(map(int, sys.stdin.readline().split()))
    if not n:
        exit(0)
    k = n[0]
    n = n[1:]
    for i, v in enumerate(n):
        visited = [0 for _ in range(len(n))]
        dfs(i, n, [])
    print('')
    
    


