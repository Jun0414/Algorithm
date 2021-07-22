
# 문제 9663번 N-Queen
# Bruteforcing(브루트포스), Back Tracking(백 트래킹)


import sys
r = sys.stdin.readline


# x번째 행 체크
def check(x):
  # 이전 행에서 놓았던 모든 퀸을 확인
  for i in range(x):
    # 같은 열인지 확인
    if row[x] == row[i]:
      return False
    # 대각선에 위치하는지 확인
    if abs(row[x] - row[i]) == x - i:
      return False
  return True


def dfs(x):
  global result

  if x == n:
    result += 1
  else:
    # x번째 행의 각 열에 둔다고 가정
    for i in range(n):
      row[x] = i
      # 해당 위치에 두어도 괜찮은 경우
      if check(x):
        # 다음 행으로 넘어가기
        dfs(x + 1)


n = int(r())
row = [0] * n
result = 0
dfs(0)
print(result)






# 입력 예시
# 8

# 출력 예시
# 92