
# 문제 1436번 영화감독 숌
# Bruteforcing(브루투포스)


import sys
r = sys.stdin.readline


n = int(r())

hell = '666'
i = 666
cnt = 0
while cnt != n:
  # 문자열로 포함여부 검사
  if hell in str(i):
    cnt += 1
  i += 1

print(i - 1)





# 입력 예시
# 2

# 출력 예시
# 1666