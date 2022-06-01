//n = 3^1 일때는 가운데를 비워두고 "별"이 찍힌 것처럼
//n = 3^i 일때는 가운데를 비워두고 "n = 3^(i-1) 일때의 별 배열"이 찍힙니다.

 
N = int(input())

def star(n):
    
    if n == 1:
        return ['*']
    stars = star(n//3)
    result = []
    for s in stars:
        result.append(s*3)
    for s in stars:
        result.append(s + ' '*(n//3) + s)
    for s in stars:
        result.append(s*3)
    return result
print('\n'.join(star(N)))

