
# 문제 5585번 거스름돈
# Greedy(그리디)


import sys
r = sys.stdin.readline


price = int(r())
change = 1000 - price

coins = [500, 100, 50, 10, 5, 1]

total = 0
for coin in coins:
  if change == 0:
    break
  if change >= coin:
    cnt = change // coin
    total += cnt
    change -= (coin * cnt)

print(total)






# 입력 예시
# 380

# 1

# 출력 예시
# 4

# 15