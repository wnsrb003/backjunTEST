import sys
from collections import defaultdict, deque
from itertools import combinations
sys.stdin = open('input.txt')

omak = [[0 for _ in range(21)] for _ in range(21)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def check(x, y):
    cnt = [0 for _ in range(8)]
    color = omak[x][y]
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        while omak[nx][ny]:
            if omak[nx][ny] == color:
                nx += dx[d]
                ny += dy[d]
                cnt[d] += 1
            else:
                break
    for i in range(4):
        if cnt[i] + cnt[i+4] == 4:
            return True
    return False

n = int(input())
for i in range(1,n+1):
    a,b = list(map(int,input().split()))
    if i % 2 == 1:
        omak[a][b] = 1
    else: 
        omak[a][b] = 2

    if check(a,b) == True:
        print(i)
        exit()
print(-1)