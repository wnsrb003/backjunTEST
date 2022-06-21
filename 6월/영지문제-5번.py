import sys

an,bn = map(int,sys.stdin.readline().split())
a = set(map(int,sys.stdin.readline().split()))
b = set(map(int,sys.stdin.readline().split()))

num = len(a&b)
print((an-num)+(bn-num))