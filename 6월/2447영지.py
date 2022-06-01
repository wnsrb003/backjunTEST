import sys

n = int(sys.stdin.readline())

#
# 1. 입력값 n을 나눌 수 없을때까지 3으로 나눈다
# 2. 3 라인으로 나눠서 출력한다. 1층 연속3번 2층 하나.빈공간.하나 3층 연속3번
star_r = ["***","* *","***"]

def star(n) :
    star_map = []
    for i in range(len(n)*3) :
        if i // len(n) == 1 :
            star_map.append(n[i%len(n)]+" "*len(n)+n[i%len(n)])
        else :
            star_map.append(n[i%len(n)]*3)
    return star_map

for _ in range(n//3-1) :
    star_r = star(star_r)

for i in star_r :
    print(i)