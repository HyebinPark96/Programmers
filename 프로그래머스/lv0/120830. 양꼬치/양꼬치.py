def solution(n, k):
    answer = 0
    target = n // 10
    answer = (n * 12000) + ((k-target) * 2000)
    
    return answer