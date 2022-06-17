from collections import defaultdict
import sys

n = int(sys.stdin.readline())
dot = defaultdict(list)
for i in range(1,n+1) :
    a,b = map(int,sys.stdin.readline().split())
    dot[i] = [a,b]

print(dot)