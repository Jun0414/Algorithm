
# 핵심 정렬
# 문제 10989번 수정렬하기 3
# Counting Sort(계수 정렬)

import sys
r = sys.stdin.readline

n = int(r())

# 저장될 수의 (최대 숫자 + 1)만큼 0으로 초기화
arr = [0] * 10001

# 해당 숫자 인덱스의 숫자를 1증가
for _ in range(n):
  data = int(r())
  arr[data] += 1

# 해당 인덱스가 count된적 있는 경우 출력
for i in range(len(arr)):
  if arr[i] != 0:
    for j in range(arr[i]):
      print(i)





# 입력 예시
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

# 출력 예시
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7