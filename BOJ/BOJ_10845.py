
# 문제 10845번 큐
# Queue(큐)

import sys
r = sys.stdin.readline

n = int(r())

queue_num = []
for _ in range(n):
  data = r().split()

  if data[0] == 'push':
    queue_num.append(int(data[1]))
  elif data[0] == 'pop':
    if len(queue_num) > 0:
      print(queue_num.pop(0))
    else:
      print(-1)
  elif data[0] == 'size':
    print(len(queue_num))
  elif data[0] == 'empty':
    if len(queue_num) == 0:
      print(1)
    else:
      print(0)
  elif data[0] == 'front':
    if len(queue_num) > 0:
      print(queue_num[0])
    else:
      print(-1)
  else: # data[0] == 'back'
    if len(queue_num) > 0:
      print(queue_num[-1])
    else:
      print(-1)





# 입력 예시
# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front

# 출력 예시
# 1
# 2
# 2
# 0
# 1
# 2
# -1
# 0
# 1
# -1
# 0
# 3