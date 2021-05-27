
# 문제 1259번 팰린드롬수
# Implementation(구현), String(문자열)


import sys
r = sys.stdin.readline

while True:
  words = r().strip()
  if words == '0':
    break

  front = 0
  back = len(words) - 1
  flag = 1
  # 인덱스 역전 현상 이전까지
  while front <= back:
    # 대칭되는 문자가 다르면 탈출
    if words[front] != words[back]:
      flag = 0
      break
    front += 1
    back -= 1

  if flag == 1:
    print('yes')
  else:
    print('no')





# 입력 예시
# 121
# 1231
# 12421
# 0

# 출력 예시
# yes
# no
# yes