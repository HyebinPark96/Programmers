def solution(n):
    answer = 0
    for num in range(n + 1): # n 포함
        if(num % 2 == 0):
            answer += num
    return answer