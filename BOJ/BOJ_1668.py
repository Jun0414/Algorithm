
# 기초 기본 탐색
# 문제 1668번 트로피 진열
# Bruteforcing(브루트포스)


import sys
r = sys.stdin.readline

n = int(r())
trophy = []
for _ in range(n):
  trophy.append(int(r()))

for _ in range(2):
  std = trophy[0]
  cnt = 1
  for i in trophy:
    if std < i:
      cnt += 1
      std = i
  print(cnt)
  trophy.reverse()





# 입력 예시
# 5
# 1
# 2
# 3
# 4
# 5

# 출력 예시
# 5
# 1