
# 문제 5397번 키로커
# Stack(스택), Deque(덱), Linked-list(연결 리스트)

import sys
r = sys.stdin.readline

case = int(r())

for _ in range(case):
  # 양쪽 공백을 제거 후 저장
  passwords = r().strip()
  
  left_stack = []
  right_stack = []
  for pw in passwords:
    # 오른쪽 커서면
    if pw == '>':
      # 오른쪽 스택에 내용이 있을 경우
      if right_stack:
        # 왼쪽으로 넘겨줌
        left_stack.append(right_stack.pop())
    # 왼쪽 커서면
    elif pw == '<':
      # 왼쪽 스택에 내용이 있을 경우
      if left_stack:
        # 오른쪽으로 넘겨줌
        right_stack.append(left_stack.pop())
    # backspace면
    elif pw == '-':
      # 왼쪽 스택에 내용이 있을 경우
      if left_stack:
        # 하나 지우기
        left_stack.pop()
    # 문자면 왼쪽 스택에 추가
    else:
      left_stack.append(pw)
  
  # 왼쪽 스택과 오른쪽 스택의 역순을 합치기
  left_stack.extend(reversed(right_stack))
  print(''.join(left_stack))


# # 시간 초과
# case = int(r())

# for _ in range(case):
#   arr = []
#   tmp = []
#   left_cnt = 0
#   heap = r()

#   while heap:
#     if len(arr) == 0 and (heap[0] == '<' or heap[0] == '>' or heap[0] == '-'):
#       heap = heap[1:]
#       continue
#     elif heap[0] == '<':
#       heap = heap[1:]
#       tmp.append(arr.pop())
#       left_cnt += 1
#     elif heap[0] == '>':
#       heap = heap[1:]
#       if left_cnt > 0:
#         left_cnt -= 1
#     elif heap[0] == '-':
#       heap = heap[1:]
#       arr.pop()
#     else:
#       arr.append(heap[0])
#       heap = heap[1:]
#       # 왼쪽 화살표 입력 이력이 있는 경우
#       while left_cnt > 0:
#         arr.append(tmp.pop())
#         left_cnt -= 1
  
#   for i in arr:
#     print(i, end='')





# 입력 예시
# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

# 출력 예시
# BAPC
# ThIsIsS3Cr3t