
# 문제 10816번 숫자 카드 2
# Binary Search(이분 탐색), Hash Set(해시맵)


import sys
r = sys.stdin.readline

n = int(r())
sang = list(map(int, r().split()))
m = int(r())
cards = list(map(int, r().split()))

hash_cnt = dict()
for i in sang:
  if i in hash_cnt:
    hash_cnt[i] += 1
  else:
    hash_cnt[i] = 1

for i in cards:
  if i in hash_cnt:
    print(hash_cnt[i], end=' ')
  else:
    print(0, end=' ')



# # 시간 초과
# for card in cards:
#   print(sang.count(card), end=' ')



# # 시간 초과
# arr = [0] * 20000002
# for i in sang:
#   if i in cards:
#     if i < 0:
#       i = 10000000 + abs(i)
#     arr[i] += 1

# for i in cards:
#   if i < 0:
#     i = 10000000 + abs(i)
#   print(arr[i], end=' ')






# 입력 예시
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

# 출력 예시
# 3 0 0 1 2 0 0 2