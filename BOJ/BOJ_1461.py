
# 문제 1461번 도서관
# Greedy(그리디), Sorting(정렬)


import sys
r = sys.stdin.readline


n, m = map(int, r().split())

book = list(map(int, r().split()))
book.append(0)
book.sort()

total = 0
# 왕복 안해도 되는 가장 먼 책을 찾았는지 여부
cnt = 0
while len(book) != 1:
  front, back = abs(book[0]), abs(book[-1])
  # m개의 책 중 가장 먼 곳의 거리 저장 여부
  flag = 0

  # 음수의 절대값이 더 큰 경우
  if front > back:
    for _ in range(m):
      # 책이 있다면
      if book:
        if book[0] == 0:
          break
        # 가장 먼 책인 경우
        if flag == 0:
          tmp = abs(book.pop(0))
          flag = 1
        # 가는 길에 가져가는 책인 경우
        else:
          book.pop(0)
    # 정리할 책 중 가장 먼 곳인 경우
    if cnt == 0:
      total += tmp
      cnt = 1
    # 정리할 책 중 가장 먼 곳이 아닌 경우
    else:
      total += (2 * tmp)
  # 양수 절대값이 더 큰 경우
  else:
    for _ in range(m):
      # 책이 있다면
      if book:
        if book[-1] == 0:
          break
        # 가장 먼 책인 경우
        if flag == 0:
          tmp = abs(book.pop(-1))
          flag = 1
        # 가는 길에 가져가는 책인 경우
        else:
          book.pop(-1)
    # 정리할 책 중 가장 먼 곳인 경우
    if cnt == 0:
      total += tmp
      cnt = 1
    # 정리할 책 중 가장 먼 곳이 아닌 경우
    else:
      total += (2 * tmp)

print(total)






# 입력 예시
# 7 2
# -37 2 -6 -39 -29 11 -28

# 출력 예시
# 131