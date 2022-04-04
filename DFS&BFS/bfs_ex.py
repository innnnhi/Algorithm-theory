from collections import deque

# 괴물피해서 미로 탈출하기
# 최단 경로 설정
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111


n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))
# print(n, m, miro)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_sol(x, y):
    que = deque()
    que.append((x, y))
    while len(que) != 0:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                que.append((nx, ny))

    return miro[n - 1][m - 1]


print(bfs_sol(0, 0))
