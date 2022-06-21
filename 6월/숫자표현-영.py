def solution(n):
    answer = 0
    for i in range(1,n//2+1) :
        temp = 0
        j= 0
        while temp < n :
            temp += (i+j)
            j+=1
            if temp == n :
                answer +=1 
    return answer+1