def solution(food):
    answer = ''
    
    left = ''
    right = ''
    
    # 왼쪽 먼저 만들고, 오른쪽은 reverse 처리
    # 짝수면 사용 가능, 홀수면 불가능
    for idx in range(len(food)):
        if idx != 0: # 첫 번째 요소는 물이므로 무시
            for _ in range(food[idx] // 2):
                left += str(idx) # 몫만 추가하고, 나머지 버리기
    
    right = left[::-1]
    
    answer = left + '0' + right
    
    return answer