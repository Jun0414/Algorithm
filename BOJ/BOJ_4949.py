
# 문제 4949번 균형잡힌 세상
# String(문자열), Stack(스택)


import sys
r = sys.stdin.readline


line = r()

while len(line) != 1 and line[0] != '.':
  stack = []
  flag = 0

  for i in line:
    if i == '(' or i == '[':
      stack.append(i)
    # 닫힌 괄호인 경우
    elif i == ')':
      # 스택이 비어있거나 짝이 안맞는 경우
      if len(stack) == 0 or stack.pop() != '(':
        flag = 1
        break
    # 닫힌 대괄호인 경우
    elif i == ']':
      # 스택이 비어있거나 짝이 안맞는 경우
      if len(stack) == 0 or stack.pop() != '[':
        flag = 1
        break
  # 불균형 또는 개수가 다른 경우
  if flag == 1 or len(stack) > 0:
    print('no')
  else:
    print('yes')
  
  line = r()






# 입력 예시
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .

# 출력 예시
# yes
# yes
# no
# no
# no
# yes
# yes