
# 핵심 고급 탐색
# 문제 1766번 문제집
# Priority Queue(우선순위 큐), Topological Sorting(위상 정렬)
# 위상정렬 : 순서의 나열 중 다음 차례 지목을 적게 받은 순서 원소부터 정렬 (사이클 구조에서는 사용 불가)
# 한번에 입력 받기 : https://johnyejin.tistory.com/62

import sys
import heapq
r = sys.stdin.readline


n, m = map(int, r().split())

arr = [[] for _ in range(n + 1)]
# 다음 차례 지목 받은 수 카운트를 위한 배열 초기화
indegree = [0] * (n + 1)

heap = []
result = []

# 지목 받은 원소 1증가
for _ in range(m):
  num1, num2 = map(int, r().split())
  arr[num1].append(num2)
  indegree[num2] += 1

# 한번도 지목 받지 않은 원소부터 힙에 추가
for i in range(1, n + 1):
  if indegree[i] == 0:
    heapq.heappush(heap, i)


while heap:
  data = heapq.heappop(heap)
  result.append(data)

  for j in arr[data]:
    # 결과에 저장한 원소가 지목한 원소 1감소
    indegree[j] -= 1
    # 감소 결과 지목한 원소가 없는 경우 힙에 추가
    if indegree[j] == 0:
      heapq.heappush(heap, j)

for i in result:
  print(i, end=' ')




# # 시간 초과 (위상정렬과 다르게 출력 됨)(그러나 이게 맞는 출력이라 생각 됨)
# def book(num):
#   if arr[num] == [0]:
#     return
#   else:
#     if len(arr[num]) == 0:
#       print(num, end=' ')
#       return
#     else:
#       while arr[num]:
#         get = heapq.heappop(arr[num])
#         book(get)
#         heapq.heappush(arr[get], 0)
#       print(num, end=' ')
#       return


# n, m = map(int, r().split())

# arr = [[] for _ in range(n + 1)]
# for _ in range(m):
#   num1, num2 = map(int, r().split())
#   heapq.heappush(arr[num2], num1)

# for i in range(1, n + 1):
#   book(i)





# 입력 예시
# 4 2
# 4 2
# 3 1

# 10 5
# 4 2
# 10 4
# 9 4
# 5 3
# 8 5

# 출력 예시
# 3 1 4 2

# 1 6 7 8 5 3 9 10 4 2