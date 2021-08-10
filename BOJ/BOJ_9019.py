
# 문제 9019번 DSLR
# Graph(그래프), BFS(너비 우선 탐색)


import sys, heapq
from collections import deque
r = sys.stdin.readline


def bfs(a, b):
  q = deque([(a, '')])
  visited = [0 for _ in range(10000)]
  visited[a] = 1

  while q:
    n, order = q.popleft()

    if n == b:
      return order
    
    nx = (2 * n) % 10000
    if visited[nx] == 0:
      visited[nx] = 1
      q.append((nx, order + 'D'))
    nx = n - 1
    if nx >= 0 and visited[nx] == 0:
      visited[nx] = 1
      q.append((nx, order + 'S'))
    if nx < 0 and visited[9999] == 0:
      visited[9999] = 1
      q.append((9999, order + 'S'))
    nx = int((n % 1000) * 10 + (n / 1000))
    if visited[nx] == 0:
      visited[nx] = 1
      q.append((nx, order + 'L'))
    nx = int((n % 10) * 1000 + (n // 10))
    if visited[nx] == 0:
      visited[nx] = 1
      q.append((nx, order + 'R'))


t = int(r())
for _ in range(t):
  a, b = map(int, r().strip().split())
  result = bfs(a, b)
  print(result)




# # 메모리 초과
# def D(arr, n):
#   new_arr = arr + 'D'
#   return (len(new_arr), new_arr, (2 * n) % 10000)

# def S(arr, n):
#   new_arr = arr + 'S'
#   if n == 0:
#     n = 9999
#   else:
#     n = n - 1
#   return (len(new_arr), new_arr, n)

# def L(arr, n):
#   new_arr = arr + 'L'
#   str_n = str(n)
#   str_n = str_n.zfill(4)
#   str_n = str_n[1:] + str_n[0]
#   return (len(new_arr), new_arr, int(str_n))

# def R(arr, n):
#   new_arr = arr + 'R'
#   str_n = str(n)
#   str_n = str_n.zfill(4)
#   str_n = str_n[3] + str_n[:3]
#   return (len(new_arr), new_arr, int(str_n))

# def bfs(a, b):
#   q = []
#   result = []
#   visited = [0 for _ in range(10000)]
#   tmp = D('', a)
#   heapq.heappush(q, tmp)
#   if tmp[2] == b: return tmp[1]
#   tmp = S('', a)
#   heapq.heappush(q, tmp)
#   if tmp[2] == b: return tmp[1]
#   tmp = L('', a)
#   heapq.heappush(q, tmp)
#   if tmp[2] == b: return tmp[1]
#   tmp = R('', a)
#   heapq.heappush(q, tmp)
#   if tmp[2] == b: return tmp[1]

#   while(q):
#     cnt, arr, num = heapq.heappop(q)

#     cnt1, arr1, num1 = D(arr, num)
#     heapq.heappush(q, (cnt1, arr1, num1))
#     if num1 == b:
#       result.append(arr1)

#     cnt2, arr2, num2 = S(arr, num)
#     heapq.heappush(q, (cnt2, arr2, num2))
#     if num2 == b:
#       result.append(arr2)

#     cnt3, arr3, num3 = L(arr, num)
#     heapq.heappush(q, (cnt3, arr3, num3))
#     if num3 == b:
#       result.append(arr3)

#     cnt4, arr4, num4 = R(arr, num)
#     heapq.heappush(q, (cnt4, arr4, num4))
#     if num4 == b:
#       result.append(arr4)

#     if result:
#       return min(result)


# t = int(r())
# for _ in range(t):
#   a, b = map(int, r().strip().split())
#   result = bfs(a, b)
#   print(result)




# 입력 예시
# 3
# 1234 3412
# 1000 1
# 1 16

# 출력 예시
# LL
# L
# DDDD