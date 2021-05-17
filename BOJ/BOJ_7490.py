
# 핵심 재귀 호출
# 문제 7490번 0 만들기
# Backtracking(백트래킹), Bruteforcing(브루트포스), Implementation(구현)
# eval() : 문자열 안의 수식을 계산해 준다


import sys
r = sys.stdin.readline

def zero(num, math, wd):
  # 처음 숫자인 경우
  if num == 1:
    wd += str(num)
    zero(num + 1, ' ', wd)
    zero(num + 1, '+', wd)
    zero(num + 1, '-', wd)
    return
  # 이후 덧셈인 경우
  elif math == '+':
    wd += math
    wd += str(num)
  # 이후 뺄셈인 경우
  elif math == '-':
    wd += math
    wd += str(num)
  # 이후 공백인 경우
  else:
    wd += math
    wd += str(num)
  
  # 마지막 숫자에 도달한 경우
  if num == n:
    # 문자열의 공백 제거
    tmp = wd.replace(' ', '')
    # eval()함수로 문자열 연산
    if eval(tmp) == 0:
      print(wd)
  # 마지막 숫자에 도달 못한 경우
  else:
    zero(num + 1, ' ', wd)
    zero(num + 1, '+', wd)
    zero(num + 1, '-', wd)

case = int(r())

for _ in range(case):
  n = int(r())
  
  wd = ''
  zero(1,'+', wd)
  print()





# 입력 예시
# 2
# 3
# 7

# 출력 예시
# 1+2-3

# 1+2-3+4-5-6+7
# 1+2-3-4+5+6-7
# 1-2 3+4+5+6+7
# 1-2 3-4 5+6 7
# 1-2+3+4-5+6-7
# 1-2-3-4-5+6+7