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
            # !! 1초 후 바로 떨어지더라도 최소 1초간 떨어지지 않은 것으로 보기 때문에 비교 전 +1 먼저 해줘야 함   
            cnt += 1
            
            # !! 떨어지는 순간 해당 반복문 빠져나오기 (중첩반복문이므로 상위 반복문의 다음 인덱스 반복 시작) 
            if i < price:
                break
        
        # cnt가 1이라면 1초만 가격이 떨어지지 않은 것으로 보며, 
        # 마지막 원소인 경우, 0초간 가격이 떨어지지 않은 것으로 봐야 하므로 마지막 원소는 조건에서 제외  
        if cnt == 1 and (len(answer) != len(prices) - 1):
            answer.append(1)
        else: 
            answer.append(cnt)
            
        # 리셋 
        cnt = 0
        
    return answer