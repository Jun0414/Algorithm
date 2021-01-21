
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
