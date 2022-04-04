# 상하좌우
# n = 5
# R R R U D D
## 1st
n = int(input())
move = input().split() # plan

#상 하 좌 우
x,y = 1,1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
use = ["U","D","L","R"]

for i in move:
    for j in range(len(use)):
        if i == use[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > n or ny < 1 or ny > 5:
        continue
    x, y = nx , ny
print(x,y)