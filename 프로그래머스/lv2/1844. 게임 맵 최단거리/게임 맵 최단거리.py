from collections import deque

def solution(maps):
    # 일차원 배열길이
    n = len(maps)
    # 이차원 배열길이
    m = len(maps[0])
    
    # 상대 팀 주위가 0일 경우, -1 리턴
    if maps[n-2][m-2] == 0 and maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0: 
        return -1
    
    # 초기화
    answer = 0
    x = 1
    y = 1
    
    # 동, 서, 남, 북 방향 설정
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y):
        # 큐 내장함수 사용
        queue = deque()
        # 큐에 넣기
        queue.append((x, y))
        
        # 큐가 비어있지 않다면 반복 실행 
        while queue: # 비어있지 않으면 true, 비어있으면 false 
            x, y = queue.popleft() # 선입선출
            
            for i in range(4):
                # 다음 값 
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 벗어나면 out
                if nx < 0 or ny < 0 or nx >= n or ny >= m: 
                    continue # 아래 코드 패스하고 다음 반복 요소로 넘어감
                
                # 벽이면 out
                if maps[nx][ny] == 0:
                    continue
            
                if maps[nx][ny] == 1: 
                    maps[nx][ny] = maps[x][y] + 1 # 최단 길이 기록하기 위해 카운트
                    queue.append((nx, ny))
        # 큐가 비면 마지막 좌표 리턴            
        return maps[n-1][m-1]      

    
    if bfs(0, 0) == 1:
        answer = -1
    else:
        answer = bfs(0, 0)
    
    
    return answer