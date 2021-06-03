
# 문제 1654번 랜선 자르기
# Binary Search(이분 탐색)


import sys
r = sys.stdin.readline


max_len = 0
def binary(min_v, max_v):
  global max_len
  
  if min_v > max_v:
    return
  mid = (min_v + max_v) // 2
  cnt = 0

  # 자른 개수 누적 저장
  for i in arr:
    cnt += i // mid

  # 원하는 개수보다 작을 시 min_v 수정
  if n > cnt:
    max_v = mid - 1
    binary(min_v, max_v)
  # 원하는 개수와 같거나 많을 시 max_v 수정 및 최대 길이 갱신
  else:
    if max_len < mid:
      max_len = mid
    min_v = mid + 1
    binary(min_v, max_v)


k, n = map(int, r().split())

arr = [int(r()) for _ in range(k)]

binary(1, max(arr))
print(max_len)







# 입력 예시
# 4 11
# 802
# 743
# 457
# 539

# 출력 예시
# 200