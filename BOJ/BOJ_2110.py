# ***어려움

# 핵심 기본 탐색
# 문제 2110번 공유기 설치
# Binary Search(이진 탐색), Parametric Search(매개 변수 탐색)
# 이진 탐색은 기본적으로 난이도가 있으니 신경 써야함


import sys
r = sys.stdin.readline

n, c = map(int, r().split())

home = []
for _ in range(n):
  home.append(int(r()))
# 좌표 순서로 정렬
home.sort()

# 원래 최소 거리는 (2번째로 작은 값 - 가장 작은 값) 이 맞다
min_gap = 1
# 최대 거리는 (가장 큰 값 - 가장 작은 값)
max_gap = home[-1] - home[0]

result = 0
while min_gap <= max_gap:
  # 우선 평균을 기준으로 시작
  mid = (min_gap + max_gap) // 2
  # 시작 지점
  value = home[0]
  
  # 공유기 설치 카운트
  cnt = 1
  for i in range(1, len(home)):
    # 거리가 예상 거리 이상일 경우 공유기 설치
    if home[i] >= value + mid:
      value = home[i]
      cnt += 1
  
  # 목표 공유기 설치 수 이상 설치한 경우
  if cnt >= c:
    # 우선 가능하므로 저장
    result = mid
    # 최소 거리가 더 먼 곳이 있나 확인
    min_gap = mid + 1
  # 목표 공유기 설치 수 미만 설치한 경우
  else:
    # 최소 거리 줄여 목표 공유기 설치 수 만족할 수 있나 확인
    max_gap = mid - 1

print(result)






# 입력 예시
# 5 3
# 1
# 2
# 8
# 4
# 9

# 출력 예시
# 3