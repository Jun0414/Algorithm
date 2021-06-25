
# 문제 7568번 덩치
# Implementation(구현), Bruteforcing(브루투포스)


import sys
r = sys.stdin.readline


n = int(r())

man = [[] for _ in range(n)]
rank_man = [1 for _ in range(n)]
for i in range(n):
  weight, height = map(int, r().split())
  man[i] = (weight, height)

for i in range(n):
  for j in range(i + 1, n):
    # i번째 수가 덩치가 큰 경우
    if man[i][0] > man[j][0] and man[i][1] > man[j][1]:
      rank_man[j] += 1
    # j번째 수가 덩치가 큰 경우
    elif man[i][0] < man[j][0] and man[i][1] < man[j][1]:
      rank_man[i] += 1

for i in range(n):
  print(rank_man[i], end=' ')






# 입력 예시
# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

# 출력 예시
# 2 2 1 2 5