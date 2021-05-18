
# 핵심 정렬
# 문제 10814번 나이순 정렬
# Sorting(정렬)

import sys
r = sys.stdin.readline

n = int(r())

arr = []
for _ in range(n):
  input_data = r().split()
  # 튜플로 저장
  arr.append((int(input_data[0]), input_data[1]))

arr = sorted(arr, key=lambda x: x[0])

for age, name in arr:
  print(age, name)


# n = int(r())

# data = dict()
# for _ in range(n):
#   age, name = map(str, r().split())
#   data[name] = int(age)

# sorted_data = sorted(data.items(), key=lambda x: x[1])

# for name, num in sorted_data:
#   print(num, name)





# 입력 예시
# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

# 출력 예시
# 20 Sunyoung
# 21 Junkyu
# 21 Dohyun