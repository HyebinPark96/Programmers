def solution(array, height):
    answer = 0
    for target in array:
        if(target > height):
            answer += 1
    return answer