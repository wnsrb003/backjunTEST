def solution(brown, yellow):
    answer = []
    mul = brown + yellow
    left, right = 0, mul

    while left <= right:
        if left * right == mul and (right + (left-2))*2 == brown:
            if not answer:
                answer = [right, left]
            else:
                answer = answer if answer[0] - answer[1] < right - left else [right, left]
        if left * right > mul:
            right -= 1
        else:
            left += 1
    return answer

print(solution(24, 24))