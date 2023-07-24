from collections import deque

def solution(prices):
    # 초기화
    answer = []
    cnt = 0
           
    # 큐 내장함수 사용
    queue = deque()

    for price in prices:
        queue.append(price)
        
    # 큐가 빌 때까지 반복
    while queue:
        price = queue.popleft()
        
        for i in queue:
            cnt += 1
            
            if i < price:
                break
        
        # cnt가 0이라면 1초만 가격이 떨어지지 않은 것으로 보며, 
        # 마지막 원소인 경우, 0초간 가격이 떨어지지 않은 것으로 봐야 하므로 마지막 원소는 조건에서 제외  
        if cnt == 1 and (len(answer) != len(prices) - 1):
            answer.append(1)
        else: 
            answer.append(cnt)
            
        # 리셋 
        cnt = 0
        
    return answer