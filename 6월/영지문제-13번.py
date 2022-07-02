from itertools import combinations
import sys

all_list = []
while 1 :
    k = list(map(int,sys.stdin.readline().split()))
    if k[0] == 0 : break
    all_list.append(k)

for k in all_list :
    a = list(combinations(k[1:],6))
    for i in a :
        print(*i)
    print()
