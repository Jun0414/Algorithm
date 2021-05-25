
# 문제 1018번 체스판 다시 칠하기
# Bruteforcing(브루트포스)


import sys
r = sys.stdin.readline

n, m = map(int, r().split())

board = []
for _ in range(n):
  board.append(r().strip())

min_cnt = 64
# 8보다 1클때마다 탐색할 행, 열 1씩 증가
for i in range(n - 7):
  for j in range(m - 7):
    cnt = 0
    # 8 X 8 행렬 조사
    for k in range(i, i + 8):
      for l in range(j, j + 8):
        # 첫 색이 검정 기준
        if (k + l) % 2 == 0:
          if board[k][l] == 'W':
            cnt += 1
        else:
          if board[k][l] == 'B':
            cnt += 1
    
    # 흰색 기준으로 한 것이 더 적으면 변경
    cnt = min(cnt, 64 - cnt)
    # 최소 변경 수 갱신
    if min_cnt > cnt:
      min_cnt = cnt

print(min_cnt)







# 입력 예시
# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# 10 13
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB

# 출력 예시
# 1

# 12