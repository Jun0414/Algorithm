
# 문제 1092번 배
# Greedy(그리디), Sorting(정렬)


import sys
r = sys.stdin.readline


def get_avg(idx):
  if (len(box) % len(limit_c[idx:])) != 0:
    avg = (len(box) // len(limit_c[idx:])) + 1
  else:
    avg = (len(box) // len(limit_c[idx:]))

  return avg


n = int(r())
limit_c = list(map(int, r().split()))
# 무게제한 내림차순 정렬
limit_c.sort()

m = int(r())
box = list(map(int, r().split()))
# box 내림차순 정렬
box.sort()

cnt = [0 for _ in range(n)]
# 제한이 낮은 것부터 실행
for i in range(len(limit_c)):
  # 최소시간으로 box를 분배할 시간 구하기
  avg = get_avg(i)
  # 최소시간 만큼 수행
  for _ in range(avg):
    # 들 수 있다면
    if limit_c[i] >= box[0]:
      # box 제거 및 카운트
      cnt[i] += 1
      box.pop(0)

# 모든 box를 나를 수 있는 경우
if not box:
  print(max(cnt))
# 모든 box를 못 나르는 경우
else:
  print(-1)





# 입력 예시
# 3
# 6 8 9
# 5
# 2 5 2 4 7

# 출력 예시
# 2