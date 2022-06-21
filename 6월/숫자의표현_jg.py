def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum_s = 0
        j = i
        while(sum_s < n):
            sum_s += j
            j+=1
        if sum_s == n:
            answer+=1
        
    return answer