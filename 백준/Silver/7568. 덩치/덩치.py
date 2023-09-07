n = int(input())

list = []
for _ in range(n): 
    weight, height = map(int, input().split())
    list.append((weight, height)) # 튜플

ranking = []
for i in range(n):
    count = 0
    for j in range(n):
        if list[i][0] < list[j][0] and list[i][1] < list[j][1]:
            count += 1
    ranking.append(count + 1)

for i in ranking:
    print(i, end=" ")
    
    