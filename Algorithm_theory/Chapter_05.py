
# 예제 5-1 (스택 p.126)

stack = []

# 삽입
stack.append(5)

# 삭제
stack.pop()



#####################################################################
# 예제 5-2 (큐 p.129)
# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

# 삽입
queue.append(5)

# 삭제
queue.popleft()

# 리스트로 변경
list(queue)



#####################################################################
# 예제 5-3 (재귀함수 p.130)

cnt = 0

def recursive_function():
    print("재귀 함수를 호출")
    global cnt
    cnt += 1

    if cnt > 4:
        return

    recursive_function()

recursive_function()



#####################################################################
# 예제 5-5 (팩토리얼 p.132)

n = int(input())

# 반복적(iterative) 계산
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial_iterative(n))

# 재귀적(recursive) 계산
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)

print(factorial_recursive(n))



#####################################################################
# 예제 5-6 (인접 행렬 p.135)

INF = 1e9

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)



#####################################################################
# 예제 5-7 (인접 리스트 p.136)

graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)


#####################################################################
# 예제 5-8 (DFS_깊이 우선 탐색 p.142)

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)



#####################################################################
# 예제 5-9 (BFS_너비 우선 탐색 p.14)
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌때까지
    while queue:
        # 하나씩 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)


#####################################################################
# 실전문제 3 (음료수 얼려 먹기 p.149)

n, m = map(int, input().split())

# 내가 작성한 답안

ice_cream = 0

graph = []
# 연달아 쓴 숫자를 리스트로 바꿔주었기 때문에 알아서 한글자씩 잘라서 넣는다(split() 불필요)
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]

def dfs(graph, x, y, visited):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0 and visited[x][y] == 0:
        visited[x][y] = 1

        dfs(graph, x - 1, y, visited)
        dfs(graph, x, y - 1, visited)
        dfs(graph, x + 1, y, visited)
        dfs(graph, x, y + 1, visited)
        return True

    return False

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            if dfs(graph, i, j, visited) == True:
                ice_cream += 1

print(ice_cream)


# 모범 답안

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 종료 조건
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 방문 안한 노드
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True

    return False

# 모든 노드에 을료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)


# 입력 예시
# 1)
# 4 5
# 00110
# 00011
# 11111
# 00000
# 2)
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111


#####################################################################
# 실전문제 4 (미로 탈출 p.152)
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌때까지
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue

            # 1인 경우에만 최단거리 추가(먼저 나온 것 부터 큐에 담기므로 중복으로 방문하더라도 처음 방문이 가장 빠르게 도착한 것)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))

# 입력 예시
# 1)
# 3 3
# 110
# 010
# 011
# 2)
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
