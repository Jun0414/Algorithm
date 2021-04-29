
# 기초 정렬
# 문제 1427번 소트인사이드
# Sorting(정렬)


import sys
r = sys.stdin.readline

num = int(r())

# 숫자로 받은 것을 문자화 시켜 한 자리씩 배열에 넣어 sorting
data = list(str(num))
data.sort(reverse=True)
for i in data:
  print(i, end='')



# # counting sort와 유사
# arr = r().strip()

# for i in range(9, -1, -1):
#   for j in arr:
#     if int(j) == i:
#       print(i, end='')




# 입력 예시
# 2143

# 출력 예시
# 4321