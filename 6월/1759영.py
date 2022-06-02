from itertools import combinations
import sys

l,c = map(int,sys.stdin.readline().split())
chars = list(sys.stdin.readline().split())

chars. sort()

def com () :
    result = []
    for i in list(combinations(chars,l)) : # 모든 조합 구하고 판별하기
        v_count = c_count = 0
        for c in i :
            if c in 'aeiou' :
                v_count += 1
            else : c_count += 1
        if v_count >= 1 and c_count > 1 :
            result.append(''.join(i))
    
    return result

for i in com() :
    print(i)

