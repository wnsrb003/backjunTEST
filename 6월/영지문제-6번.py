import sys

an,bn = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))


for i in sorted(a+b) :
    print(i,end=" ")