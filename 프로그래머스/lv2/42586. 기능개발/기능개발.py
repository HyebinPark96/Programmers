from collections import deque
def solution(progresses, speeds):
    answer = []
    
    # 선입선출 => 큐 사용
    queue1 = deque();
    
    queue2 = deque();
    
    day = 1
    
    # 큐 삽입
    for progress in progresses:
        queue1.append(progress);
    
    for speed in speeds: 
        queue2.append(speed);
    
    # 각 배포마다 배포되는 작업 카운팅 
    cnt = 0
    
    # 큐 빌 때까지 반복
    while queue1: 
        if queue1[0] + (queue2[0] * day) >= 100:
            queue1.popleft()
            queue2.popleft()
            cnt += 1
            if len(queue1) == 0:
                answer.append(cnt)
        else:
            if cnt > 0: 
                answer.append(cnt)
            cnt = 0
            day += 1
            
    return answer