import heapq
import sys

n = int(sys.stdin.readline())
q = []
for _ in range(n) :
    a = list(map(int,sys.stdin.readline().split()))
    for i in a :
        heapq.heappush(q,i)
        if len(q) > n :
            heapq.heappop(q)

print(q[0]) 