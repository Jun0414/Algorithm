
# 예제 9-1 (간단한 다익스트라 알고리즘 p.237)

import sys
input = sys.stdin.readline
# 무한을 의미하는 10억 값 설정
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문 여부 체크 리스트
visited = [False] * (n + 1)
# 최단거리 테이블 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    # a노드에서 b노드로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    # 최단거리가 가장 짧은 노드(인덱스)
    index = 0

    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드를 제외한 n - 1개의 노드에서 반복
    for i in range(n - 1):
        # 현재 최단거리가 가장 짧은 노드를 찾아, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기위한 최단거리 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우
    else:
        print(distance[i])


# 예제 9-2 (개선된 다익스트라 알고리즘 p.248)
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력
n, m = map(int, input().split())
# 시작 노드번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def improve_dijkstra(start):
    q = []

    # 시작노드로 가기 위한 최단경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거ㅣ가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

improve_dijkstra(start)

# 모든 노드로 각 위한 최단거리 출력
for i in range(1, n + 1):
    # 도달할 수 없으면 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있으면 거리 출력
    else:
        print(distance[i])


# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2




#####################################################################
# 예제 9-3 (플로이드 워셜 알고리즘 p.257)

# 무한을 10억으로 초기화
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용은 c라는 의미
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행 (경유가 비용이 적을 시 갱신)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력하는 반복문
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없을 시, 무한 출력
        if graph[a][b] == INF:
            print('INFINITY')
        # 도달할 수 있을 시, 거리 출력
        else:
            print(graph[a][b], end='\t')
    print()

# 입력 예시
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2


