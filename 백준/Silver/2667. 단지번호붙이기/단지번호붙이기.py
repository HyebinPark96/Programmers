answer = 0
x = 0
y = 0

# 가로 * 세로
n = int(input())

# 단지 정보
arr = []

# 단지당 집 개수를 담을 배열
cntArr = []

# 단지수
cpxCnt = 0

# 단지당 집 개수
house = 0

# 단지 추가
for i in range(n):
  arr.append(list(map(int, input())))

# 상,하,좌,우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global house

  # 범위 벗어나면 out
  if x < 0 or y < 0 or x >= n or y >= n:
    return False

  # 집 있는 곳이라면 방문처리
  if arr[x][y] == 1:
    arr[x][y] = 0 # 방문처리
    house += 1
    # 상하좌우 재귀
    dfs(x -1, y)
    dfs(x, y-1)
    dfs(x +1, y)
    dfs(x, y+1)
    return True
  return False


for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      cpxCnt += 1
      cntArr.append(house)
      house = 0
      
# 오름차순 정렬
cntArr.sort() 

print(cpxCnt)
for i in cntArr:
  print(int(i))
