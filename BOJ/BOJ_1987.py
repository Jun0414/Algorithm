
# 문제 1987번 알파벳
# Graph(그래프), Back Tracking(백 트래킹), dfs(깊이 우선 탐색)


import sys
r = sys.stdin.readline


directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(x, y):
  global result

  q = set()
  # 첫 스텝은 0,0 좌표
  q.add((x, y, arr[x][y]))

  while q:
    x, y, step = q.pop()
    # 현재까지 가장 긴 문자열 길이 저장
    result = max(result, len(step))

    for dx, dy in directions:
      nx, ny = (x + dx), (y + dy)

      # 범위 안에 있고, 지나지 않은 알파벳이면
      if nx >= 0 and nx < row and ny >= 0 and ny < col and arr[nx][ny] not in step:
        q.add((nx, ny, step + arr[nx][ny]))

row, col = map(int, r().split())
arr = []
for _ in range(row):
  arr.append(r())

result = 0
bfs(0, 0)
print(result)



# # 내가 짠 코드
# directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# def dfs(x, y, alpha):
#   global max_str
#   alpha = alpha + board[x][y]
#   max_str = max(max_str, len(alpha))

#   for dx, dy in directions:
#     nx, ny = (x + dx), (y + dy)
#     if nx  >= 0 and ny >= 0 and nx < row and ny < col and board[nx][ny] not in alpha:
#       dfs(nx, ny, alpha)


# row, col = map(int, r().split())

# board = []
# for _ in range(row):
#   board.append(r())

# max_str = 0
# dfs(0,0, '')
# print(max_str)







# 입력 예시
# 2 4
# CAAB
# ADCB

# 3 6
# HFDFFB
# AJHGDH
# DGAGEH

# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH

# 출력 예시
# 3

# 6

# 10