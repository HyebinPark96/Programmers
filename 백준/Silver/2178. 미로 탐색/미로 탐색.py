# 큐 -> deque 라이브러리 사용 
from collections import deque

# 도착 지점
N, M = map(int, input().split())

# 이차원 배열 생성
graph = []
for i in range(N): 
    graph.append(list(map(int, input())))

# 상하좌우 이동 시 변화하는 좌표  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    # 튜플 데이터 삽입
    queue.append((x,y)) 
    
    # 상하좌우 탐색
    while queue: # 큐 빌 때까지 반복 
        x, y = queue.popleft() 
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 벗어날 경우
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue # 아래 코드 무시하고 다음 반복 요소로 이동 
            if graph[nx][ny] == 0:
                continue 
            if graph[nx][ny] == 1: # 아직 안지난 칸이라면 1이므로 큐에 넣기 
                graph[nx][ny] = graph[x][y] + 1 # 최단거리 기록 
                queue.append((nx, ny))
    
    
    # 큐가 다 비면 리턴할 코드 
    return graph[N-1][M-1] # 도착지점 값 리턴 
    
# 0,0 좌표부터 출발 
print(bfs(0,0))

# BFS 알고리즘이 최단거리를 증명할 수 있는 이유 
# 경로가 여러개라도 각 경로마다 이동거리를 +1씩 기록하면서 이동하므로, (최단거리가 아닌 경로에서 이동할 때) 칸의 값이 2 이상이라면(= 이미 지나간 칸이라면) 큐에 삽입 안하고, 최단거리에 기록되지 못한다.   
# 참조 https://ansohxxn.github.io/programmers/114/


