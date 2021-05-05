
# 문제 11866번 요세푸스 문제 0
# Queue(큐)


import sys
r = sys.stdin.readline

n, k = map(int, r().split())
people = [x for x in range(1, n + 1)]

result = []
index = 0
while people:
  # 인덱스를 k만큼 카운트 후, 배열의 길이만큼 나눠주면
  # 순환 구조가 된다
  index = (index + k - 1) % len(people)
  result.append(str(people.pop(index)))

print('<' + ', '.join(result) + '>')





# 입력 예시
# 7 3

# 출력 예시
# <3, 6, 2, 7, 5, 1, 4>