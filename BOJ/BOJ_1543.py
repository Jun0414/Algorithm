
# 기초 기본 탐색
# 문제 1543번 문서 검색
# Bruteforcing(브루트포스), String(문자열)


import sys
r = sys.stdin.readline

doc = r().strip()
find = r().strip()

i = 0
cnt = 0
while i < len(doc):
  # 동일한 단어를 찾으면 카운트 후, 단어 길이만큼 이동
  if doc[i:(i + len(find))] == find:
    cnt += 1
    i += len(find)
  # 아니면 한 칸 이동
  else:
    i += 1

print(cnt)





# 입력 예시
# ababababa
# aba

# a a a a a
# a a

# 출력 예시
# 2

# 2