
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



