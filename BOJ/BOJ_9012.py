
# 문제 9012번 괄호
# Stack(스택), String(문자열)

import sys
r = sys.stdin.readline

t = int(r())

for _ in range(t):
  sen = r().strip()

  cnt = 0
  for word in sen:
    if word == '(':
      cnt += 1
    else: # word == ')'
      cnt -= 1
      # ) 먼저 사용된 경우
      if cnt < 0:
        break
  
  if cnt == 0:
    print('YES')
  else:
    print('NO')









# 입력 예시
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# 3
# ((
# ))
# ())(()

# 출력 예시
# NO
# NO
# YES
# NO
# YES
# NO

# NO
# NO
# NO