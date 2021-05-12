
# 문제 1966번 프린터 큐
# Queue(큐)

import sys
r = sys.stdin.readline

case = int(r())

for _ in range(case):
  n, m = list(map(int, r().split()))
  queue = list(map(int, r().split()))
  # enumerate로 인덱스 생성 후, 튜플로 저장
  queue = [(i, idx) for idx, i in enumerate(queue)]

  cnt = 0
  while True:
    # queue안의 가장 큰 값과 동일하다면 (key를 기준으로 탐색)
    if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
      cnt += 1
      # 그 값이 찾고자 하는 값이면
      if queue[0][1] == m:
        print(cnt)
        break
      # 찾고자하는 값이 아니면
      else:
        queue.pop(0)
    # 가장 큰 값이 아니면
    else:
      queue.append(queue.pop(0))


# case = int(r())

# for _ in range(case):
#   n, m = map(int, r().split())
#   arr = list(map(int, r().split()))
#   cnt = 0

#   # 원소가 1개 이하인 경우 1 출력
#   if len(arr) <= 1:
#     print(1)
#     continue

  
#   while arr:
#     biggest = True
#     # 뒤에 큰 수가 있는지 확인
#     for j in range(1, len(arr)):
#       if arr[0] < arr[j]:
#         biggest = False
#         break
    
#     # 뒤에 큰 수가 없다면
#     if biggest:
#       arr.pop(0)
#       cnt += 1

#       # 내가 찾고자 한 수라면
#       if m == 0:
#         print(cnt)
#         break
#       # 내가 찾고자 한 수가 아니라면
#       else:
#         m -= 1
#     # 뒤에 큰 수가 있다면
#     else:
#       arr.append(arr.pop(0))
      
#       # 배열의 맨 마지막 index
#       if m == 0:
#         m = len(arr) - 1
#       # index 한칸 앞으로 이동
#       else:
#         m -= 1




# 입력 예시
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# 출력 예시
# 1
# 2
# 5