import sys
sys.stdin = open('input.txt')
from collections import defaultdict
N, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    string = sys.stdin.readline().strip()
    string = string[3:len(string)-4]
    arr.append(set(string))
print(arr)

dic = defaultdict(int)