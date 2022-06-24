from itertools import permutations
import sys

n = int(sys.stdin.readline())
nlist = []
for i in range(1,n+1) :
    nlist.append(i)
nper = list(permutations(nlist,n))
for i in nper :
    print(*i)