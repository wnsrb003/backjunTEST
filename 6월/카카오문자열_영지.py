def solution(s):
    answer = ''
    stack = []
    nums = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for x in s :
        if(x >= '0' and x <= '9'):
            answer += x
        else :
            stack.append(x)
            if len(stack) > 2 and ''.join(stack) in nums :
                num = nums[''.join(stack)]
                answer += num
                stack = []
    return int(answer)
