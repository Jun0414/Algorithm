
# 문제 2292번 벌집
# Math(수학)


import sys
r = sys.stdin.readline


n = int(r())

sum = 1
cnt = 1

# 6의 배수만큼 더해주며 증가
while sum < n:
  sum += (6 * cnt)
  cnt += 1
print(cnt)







# 입력 예시
# 13

# 58

# 출력 예시
# 3

# 5