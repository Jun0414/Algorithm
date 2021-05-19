
# 핵심 고급 정렬
# 문제 11004번 K 번째 수
# Sorting(정렬)


import sys
r = sys.stdin.readline

n, k = map(int, r().split())
arr = list(map(int, r().split()))

arr.sort()
print(arr[k - 1])




# 입력 예시
# 5 2
# 4 1 2 3 5

# 출력 예시
# 2