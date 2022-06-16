from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth = defaultdict(list)
    
    for i in clothes :
        cloth[i[1]].append(i[0])
    for i in cloth :
        answer *= (len(cloth[i])+1)
        
    return answer-1