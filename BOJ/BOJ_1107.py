
# 문제 1107번 리모컨
# Bruteforcing(브루투포스)


import sys
r = sys.stdin.readline


n = int(r())
m = int(r())

can_nums = set(str(i) for i in range(10))
can_nums -= set(map(str, r().split()))

curr_channel = 100
# 현재 채널에서 최소값
min_cnt = abs(n - curr_channel)

# 원하는 채널 번호보다 큰 숫자에서 더 적은 회수로 가능한 경우가 있으므로 50만의 2배 100만으로 세팅
for channel in range(1_000_000):
  # 선정한 채널의 자릿 수 만큼
  for j in range(len(str(channel))):
    # 번호가 누를 수 없는 경우
    if str(channel)[j] not in can_nums:
      break
    # 선정한 모든 숫자가 사용 가능한 경우
    elif len(str(channel)) - 1 == j:
      # 최소값 갱신(기존값, +-로 이동한 개수와 숫자로 한번에 이동할때 누른 버튼 개수 합)
      min_cnt = min(min_cnt, abs(n - channel) + len(str(channel)))
print(min_cnt)






# 입력 예시
# 5457
# 3
# 6 7 8

# 100
# 5
# 0 1 2 3 4

# 500000
# 8
# 0 2 3 4 6 7 8 9

# 출력 예시
# 6

# 0

# 11117