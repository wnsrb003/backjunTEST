import sys
sys.stdin = open('input.txt')

from collections import deque
arr = deque(list(sys.stdin.readline().strip()))
N = int(input())
temp_arr = deque()
for _ in range(N):
    put = input()
    if put[0] == 'P':
        arr.append(put[2])
    elif put[0] == 'L':
        if arr:
            temp_arr.appendleft(arr.pop())
    elif put[0] == 'D':
        if temp_arr:
            arr.append(temp_arr.popleft())
    else:
        if arr:
            arr.pop()
print(''.join(arr + temp_arr))