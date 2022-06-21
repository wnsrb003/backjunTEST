import sys
sys.stdin = open('input.txt');

N = int(input())
target = int(input())

dx = [0, 1]
dy = [1, 0]
graph = [[0 for i in range(N*N+1)] for _ in range(N*N+1)]
start = [N // 2, N // 2]
for i in range(N):
  for j in range(i+1, N+1):
      nx = start[0] + dx[0]
      ny = start[1] + dy[0]
      graph[nx][ny] = 
