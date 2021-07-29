
# 문제 5430번 AC
# Deque(덱), String(문자열)


import sys, re
r = sys.stdin.readline


t = int(r())

for _ in range(t):
  func = r().strip()
  # 두번 연속 뒤집기는 생략
  func = func.replace('RR', '')
  cnt = int(r())
  # r'\d+' : 1회 이상 반복되는 숫자들에 대한 패턴 의미
  # nums = re.findall(r'\d+', r().strip())
  nums = r().rstrip()[1:-1].split(',')

  rev = False
  front = 0
  rear = 0
  for i in range(len(func)):
    # 뒤집기인 경우
    if func[i] == 'R':
      rev = not rev
    # 삭제인 경우
    else:
      # 정방향인 경우
      if rev == False:
        front += 1
      # 역방향인 경우
      else:
        rear += 1
  
  # 삭제 요청 개수가 원래 개수와 같거나 작은 경우
  if front + rear <= cnt:
    result = nums[front:(cnt - rear)]
    
    # 역방향인 경우
    if rev:
      print('[' + ','.join(result[::-1]) + ']')
    # 정방향인 경우
    else:
      print('[' + ','.join(result) + ']')
  # 원래 개수보다 더 많이 삭제를 요청한 경우
  else:
    print('error')





# 입력 예시
# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []

# 출력 예시
# [2,1]
# error
# [1,2,3,5,8]
# error