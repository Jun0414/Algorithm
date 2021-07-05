
# 문제 2212번 센서
# Greedy(그리디), Sorting(정렬)


import sys
r = sys.stdin.readline


n = int(r())
k = int(r())

sensors = list(map(int, r().split()))
sensors.sort()

# 기지국이 더 많은 경우(처리 안하면 런타임에러(ValueError))
if k >= n:
  print(0)
  sys.exit()

center = []
for i in range(n - 1):
  center.append(abs(sensors[i] - sensors[i + 1]))

for _ in range(k - 1):
  far = max(center)
  center.remove(far)

print(sum(center))






# 입력 예시
# 6
# 2
# 1 6 9 3 6 7

# 출력 예시
# 5