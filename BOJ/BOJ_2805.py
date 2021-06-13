
# 문제 2805번 나무 자르기
# Binary Search(이분 탐색)


import sys
r = sys.stdin.readline


max_len = 0
def binary(min_v, max_v):
  global max_len

  if min_v > max_v:
    return

  mid = (min_v + max_v) // 2
  get_len = 0

  for i in trees:
    # 음수가 더해지는 경우 방지
    if mid < i:
      get_len += (i - mid)
  
  # 원하는 길이가 나오지 않은 경우 min_v 수정
  if m > get_len:
    max_v = mid - 1
    binary(min_v, max_v)
  # 원하는 길이 이상 나온 경우 max_v 수정 및 최대 길이 갱신
  else:
    if max_len < mid:
      max_len = mid
    min_v = mid + 1
    binary(min_v, max_v)



n, m = map(int, r().split())
trees = list(map(int, r().split()))

binary(0, max(trees))
print(max_len)







# 입력 예시
# 4 7
# 20 15 10 17

# 출력 예시
# 15