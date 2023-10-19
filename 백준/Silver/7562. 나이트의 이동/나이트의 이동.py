from collections import deque

# 이동가능한 8가지 방향 
dx = [+2, +2, -2, -2, +1, +1, -1, -1]
dy = [-1, +1, -1, +1, -2, +2, -2, +2]

def bfs(sx, sy, ex, ey, l):
    queue = deque()
    queue.append((sx, sy))
    
    while queue:
        # 튜플데이터를 큐에서 꺼내기
        x, y = queue.popleft()
        
        # 목표 칸 도착
        if x == ex and y == ey:
            # 시작 칸 1로 설정했으므로 총 카운트는 -1 해줘야 함
            print(graph[x][y] - 1)
            return True
        
        # 8가지 방향 방문처리 
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue # 아래 코드 무시하고 다음 반복 요소로 넘어감
            if graph[nx][ny] == 0: # 방문처리 안된 칸이라면 
                # 방문처리 (++1 카운팅)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return False        

# 테스트케이스 개수 
testCnt = int(input())
for test in range(testCnt):
    # 체스판 한 변의 길이 
    l = int(input())
    # 현재 있는 칸
    sx, sy = map(int, input().split())
    # 이동하려고 하는 칸
    ex, ey = map(int, input().split())
    
    # 이차원 배열 생성
    graph = [[0] * l for _ in range(l)]
    
    # 시작 칸은 1로 설정
    graph[sx][sy] = 1
   
    bfs(sx, sy, ex, ey, l)





