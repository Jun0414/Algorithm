
# 문제 10828번 스택
# Stack(스택)

import sys
r = sys.stdin.readline

n = int(r())

stack_num = []
for _ in range(n):
  data = r().split()

  if data[0] == 'push':
    stack_num.append(int(data[1]))
  elif data[0] == 'pop':
    if len(stack_num) > 0:
      print(stack_num.pop())
    else:
      print(-1)
  elif data[0] == 'size':
    print(len(stack_num))
  elif data[0] == 'empty':
    if len(stack_num) == 0:
      print(1)
    else:
      print(0)
  else: # data[0] == 'top'
    if len(stack_num) > 0:
      print(stack_num[-1])
    else:
      print(-1)





# 입력 예시
# 14
# push 1
# push 2
# top
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
# top

# 7
# pop
# top
# push 123
# top
# pop
# top
# pop

# 출력 예시
# 2
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
# 123
# 123
# -1
# -1