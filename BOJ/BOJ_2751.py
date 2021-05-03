
# 핵심 고급 정렬
# 문제 2751번 수 정렬하기 2
# Sorting(정렬)


import sys
r = sys.stdin.readline

n = int(r())

arr = []
for _ in range(n):
  arr.append(int(r()))

arr.sort()
for i in arr:
  print(i)



# # 병합 정렬
# def merge(arr):
#   if len(arr) <= 1:
#     return arr
  
#   mid = len(arr) // 2
#   left = merge(arr[:mid])
#   right = merge(arr[mid:])
  
#   total = []
#   while len(left) > 0 and len(right) > 0:
#     if left[0] < right[0]:
#       total.append(left.pop(0))
#     else:
#       total.append(right.pop(0))

#   if len(left) > 0:
#     total.extend(left)
#   elif len(right) > 0:
#     total.extend(right)

#   return total


# n = int(r())

# arr = []
# for _ in range(n):
#   arr.append(int(r()))

# arr = merge(arr)
# for i in arr:
#   print(i)





# 입력 예시
# 5
# 5
# 4
# 3
# 2
# 1

# 출력 예시
# 1
# 2
# 3
# 4
# 5

