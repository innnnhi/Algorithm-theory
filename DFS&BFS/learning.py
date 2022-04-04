from collections import deque

# 그래프 '탐색' 알고리즘 : DFS/ BFS

# 자료구조
# 1. 스택 자료구조 : 선입후출 (먼저 넣은거 나중에 나감) = 입구 출구 동일
# 2. 큐 : 선입선출 자료구조 = 입구 출구가 모두 뚫려있는 터널과 같은 형태
# 큐 vs 리스트 : 기능적으로 큐의 자료구조 형태를 리스트를 이용해서 구현할 수 있지만, 시간복잡도가 다름
# # 리스트의 시간복잡도가 큐를 사용했을때의 시간복잡도 보다 높아서 리스트보다는 큐사용
#
# from collections import deque
#
# que = deque()
#
# que.append(5)
# que.append(2)
# que.append(3)
# que.popleft()
# print(que)
# que.append(7)
# que.append(8)
# print(que)
# que.popleft()
# print(que)
# que.reverse()
# print(que)

# 재귀함수 : 자기 자신을 다시 호출하는 함수를 의미함
# 파이썬에서는 어느정도 출력하다가 [최대 재귀 깊이 초과 메세지]가 출력됨
# 재귀함수가 무한루프'처럼' 돌 수 있기 때문에 재귀함수 문제풀이에서 사용할 때는 반드시! 재귀함수 종
# 료 조건을 반드시 명시해야함 >> 종료조건 명시 x -> 함수가 무한히 호출 될 수 있다.

# 종료조건 명시 x 재귀함수 예제
# def recrusive_function():
#     print("재귀 함수 호출")
#     recrusive_function()
#
# print(recrusive_function())
# RecursionError: maximum recursion depth exceeded while calling a Python object

# 종료조건 명시 o 재귀함수 예제
# def recrusive_function(i):
#     if i == 100: # 재귀함수 종료조건 명시
#         return
#     print(f"{i}번째 재귀함수에서 {i+1}번쨰 재귀함수를 호출합니다.")
#     recrusive_function(i+1) # 재귀함수 부르고
#     print(i,'번째 재귀함수 종료')
#
# print(recrusive_function(1))


# 팩토리얼 구현 : 재귀함수 & 반복문으로 구현
# 반복문
# def repeat_function(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#     return result
# print(repeat_function(5))

# 재귀함수
# def recursive_function(n): 3 2 1
#     if n <= 1:
#         return 1
#     return n * (recursive_function(n-1)) 3 * f(2) = 2 * f(1) = 1  ==> 3 * 2 * 1
# print(recursive_function(5))

# 유클리드 호제법
# def u_h(a,b):
#     # print(a, b)
#     if a % b == 0 :
#         return b
#     else:
#         r = a % b # b % r
#         return u_h(b, r)
#
# print(u_h(192,161))

# dfs(depth first search)는 깊이 우선탐색 > 깊은 부분을 우선적으로 탐색하는 알고리즘
# dfs는 스택자료구조(or 재귀함수)를 이용
# 과정 :
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면
# 그 노드를 스택에 넣고 방문 처리함. 방문하지 않은 인접 노드가 없으면 최상단 노드를 꺼낸다
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
# 사용하는 경우 : 모든 노드를 방문하고자 하는 경우에 이방법 선택

# dfs
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],  # 1번 기준
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현 ( 1차원 리스트)
visited = [False] * 9


#
# def dfs(graph,v,visted):
#     visted[v] = True
#     # print(visted[v] , v, "자 지금여기부터 출발")
#     print(v, end=" ")
#     for i in graph[v]:
#         # print(i,"지금 내가보고 갈곳을 정하는 곳")
#         if not visted[i]:
#             # print(i, "아직 방문 안한 곳")
#             dfs(graph,i,visted)
#             # print(i, "다시 돌아옴")
#
# print(dfs(graph,1,visited))

# bfs ( breadth first search)
# bfs 는 너비 우선 탐색. 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# bfs는 "큐 자료구조"를 이용
# 과정 :
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸뒤에 해당 노드의 인접 노드 중에서
# 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 더이상 2.의 과정을 수행할수 없을때 까지 반복
# 특정 조건에서의 최단경로 구하는 목적으로 많이 출제되고 이를 효율적으로 풀수 있음

# BFS
def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


print(bfs(graph, 1, visited))
