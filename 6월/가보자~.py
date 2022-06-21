def solution(brown, yellow):
    answer = []
    def check (x,y) :
        if (x-2)*(y-2) == yellow and 2*x+2*(y-2) == brown :
            return True
        return False
    
    d = brown+yellow
    for i in range(1,d+1) :
        if d % i == 0 :
            if check(i,d//i) :
                answer = [d//i,i]
                break
    
    return answer