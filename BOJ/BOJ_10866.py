
# 문제 10866번 덱
# Deque(덱)

import sys
from collections import deque 
r = sys.stdin.readline

n = int(r())

deque_num = deque([])
for _ in range(n):
  data = r().split()

  if data[0] == 'push_front':
    deque_num.appendleft(int(data[1]))
  elif data[0] == 'push_back':
    deque_num.append(int(data[1]))
  elif data[0] == 'pop_front':
    if len(deque_num) > 0:
      print(deque_num.popleft())
    else: print(-1)
  elif data[0] == 'pop_back':
    if len(deque_num) > 0:
      print(deque_num.pop())
    else: print(-1)
  elif data[0] == 'size':
    print(len(deque_num))
  elif data[0] == 'empty':
    if len(deque_num) == 0:
      print(1)
    else:
      print(0)
  elif data[0] == 'front':
    if len(deque_num) > 0:
      print(deque_num[0])
    else:
      print(-1)
  else: # data[0] == 'back'
    if len(deque_num) > 0:
      print(deque_num[-1])
    else:
      print(-1)





# 입력 예시
# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

# 22
# front
# back
# pop_front
# pop_back
# push_front 1
# front
# pop_back
# push_back 2
# back
# pop_front
# push_front 10
# push_front 333
# front
# back
# pop_back
# pop_back
# push_back 20
# push_back 1234
# front
# back
# pop_back
# pop_back

# 출력 예시
# 2
# 1
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

# -1
# -1
# -1
# -1
# 1
# 1
# 2
# 2
# 333
# 10
# 10
# 333
# 20
# 1234
# 1234
# 20