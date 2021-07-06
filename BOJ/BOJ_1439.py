
# 문제 1439번 뒤집기
# Greedy(그리디)


import sys
r = sys.stdin.readline


s = r()

cnt = [0, 0]
tmp = s[0]
for i in s:
  if i != tmp:
    cnt[int(tmp)] += 1
    tmp = i
print(min(cnt))





# 입력 예시
# 0001100

# 출력 예시
# 1