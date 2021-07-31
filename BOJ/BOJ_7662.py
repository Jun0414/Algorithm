
# 문제 7662번 이중 우선순위 큐
# Priority Queue(우선순위 큐)


import sys, heapq
r = sys.stdin.readline


t = int(r())

for _ in range(t):
  min_h = []
  max_h = []
  # 최소힙과 최대힙 동기화 위해
  visited = [False] * 1_000_001

  k = int(r())
  for i in range(k):
    func, num = map(str, r().strip().split(' '))

    if func == 'I':
      heapq.heappush(min_h, (int(num), i))
      heapq.heappush(max_h, (-(int(num)), i))
      visited[i] = True
    else:
      # 최소값 삭제 시
      if num == '-1':
        # 최소힙의 최소값이 최대힙에서 삭제한 숫자인 경우
        while min_h and not visited[min_h[0][1]]:
          # 동기화 작업(삭제)
          heapq.heappop(min_h)
        # 실제 최소값 삭제
        if min_h:
          visited[min_h[0][1]] = False
          heapq.heappop(min_h)
      # 최대값 삭제 시
      else:
        # 최대힙의 최대값이 최소힙에서 삭제한 숫자인 경우
        while max_h and not visited[max_h[0][1]]:
          # 동기화 작업(삭제)
          heapq.heappop(max_h)
        # 실제 최대값 삭제
        if max_h:
          visited[max_h[0][1]] = False
          heapq.heappop(max_h)
  
  # 마지막 삭제한 숫자 동기화(혹시 모르니 각각)
  while min_h and not visited[min_h[0][1]]:
    heapq.heappop(min_h)
  while max_h and not visited[max_h[0][1]]:
    heapq.heappop(max_h)

  # 남은 힙의 최대값과 최소값 출력
  if min_h and max_h:
    print(-max_h[0][0], min_h[0][0])
  # 없을 시 출력
  else:
    print('EMPTY')






# # 시간 초과
# t = int(r())

# for _ in range(t):
#   q = []
#   k = int(r())

#   for _ in range(k):
#     func, num = map(str, r().strip().split(' '))

#     if func == 'I':
#       heapq.heappush(q, int(num))
#     else:
#       if q:
#         if num == '-1':
#           heapq.heappop(q)       
#         else:
#           q = heapq.nlargest(len(q), q)[1:]
#           heapq.heapify(q)
  
#   if len(q) == 0:
#     print('EMPTY')
#   else:
#     tmp = q[0]
#     print(heapq.nlargest(1, q)[0], tmp)







# # 시간 초과
# def que(q):
#   tmp = []
#   while q:
#     heapq.heappush(tmp, -(heapq.heappop(q)))
#   return tmp

# t = int(r())

# for _ in range(t):
#   q = []
#   ascend = True
#   k = int(r())
#   for _ in range(k):
#     func, num = map(str, r().strip().split(' '))
#     if func == 'I':
#       if ascend:
#         heapq.heappush(q, int(num))
#       else:
#         heapq.heappush(q, -int(num))
#     else:
#       if q:
#         if num == '-1':
#           if ascend:
#             heapq.heappop(q)
#           else:
#             q = que(q)
#             heapq.heappop(q)
#             ascend = True        
#         else:
#           if ascend:
#             q = que(q)
#             heapq.heappop(q)
#             ascend = False
#           else:
#             heapq.heappop(q)

#   if len(q) == 0:
#     print('EMPTY')
#   else:
#     if ascend:
#       tmp = q[0]
#       q = que(q)
#       print(-q[0], tmp)
#     else:
#       tmp = -q[0]
#       q = que(q)
#       print(tmp, q[0])









# 입력 예시
# 2
# 7
# I 16
# I -5643
# D -1
# D 1
# D 1
# I 123
# D -1
# 9
# I -45
# I 653
# D 1
# I -642
# I 45
# I 97
# D 1
# D -1
# I 333

# 출력 예시
# EMPTY
# 333 -45