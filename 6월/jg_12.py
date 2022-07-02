import sys
sys.stdin = open('input.txt')
N = int(input())

arr = [i for i in range(1, N+1)]
result = []
def dfs(i, stack):
    if i > N+1:
        return
    stack.append(i)
    if len(stack) == N:
        result.append(stack[:])
        return
    visited[i] = True
    for j in range(1, N+1):
        if not visited[j]:
            dfs(j, stack)
            visited[j] = 0
            stack.pop()
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    dfs(i, [])
for r in result:
    print(*r)    