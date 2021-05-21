
# 기초 기본 탐색
# 문제 1302번 베스트셀러
# Hash Set(해시맵), Sorting(정렬)


import sys
r = sys.stdin.readline

n = int(r())

book = {}
for _ in range(n):
  name = r().strip()
  
  if name in book:
    book[name] += 1
  else:
    book[name] = 1

# 가장 많이 팔린 책의 수
max_num = max(book.values())

arr = []
for name, num in book.items():
  if max_num == num:
    arr.append(name)

# 많이 팔린 책 이름 사전순 중 첫번째 출력
print(sorted(arr)[0])






# 입력 예시
# 5
# top
# top
# top
# top
# kimtop

# 출력 예시
# top