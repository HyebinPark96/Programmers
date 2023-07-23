def solution(numbers, target):
    answer = 0
    
    def dfs(level, sum):
        nonlocal answer
        if level == len(numbers):
            if sum == target:
                answer += 1
            return True
        
        dfs(level + 1, sum + numbers[level])
        dfs(level + 1, sum - numbers[level])
            
    dfs(0, 0)

    return answer