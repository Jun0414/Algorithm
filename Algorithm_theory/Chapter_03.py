
# 예제 3-1 (거스름돈 p.87)
# 그리디 -> 다이나믹 프로그래밍 or 그래프

change = 1260
count = 0
coin_type = [500, 100, 50, 10]  #왜 {}로하면 14가 뜨고, []로하면 6이 뜨지..?

for coin in coin_type:
    count += change // coin
    change %= coin

print(count)



#####################################################################
# 실전문제 2 (큰 수의 법칙 p.92)
# 가장 큰 수와 두번째 큰 수만 활용

# 공백 구분으로 입력 받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
num = data[0]


# 내가 작성한 답안
sum = 0
_k = k

for _ in range(m):
    if num <= data[0] and _k != 0:
        num = data[0]
        _k -= 1
    if _k == 0:
        num = data[1]
        _k = 3
    sum += num

print(sum)


# 효율적인 답안
sum = 0

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
# 딱 나누어 떨어지지 않았을 경우 그 만큼 큰 수를 더해주기위해
count += m % (k + 1)

sum += (count) * data[0]
sum += (m - count) * data[1]

print(sum)



#####################################################################
# 실전문제 3 (숫자 카드 게임 p.96)

n, m = map(int, input().split())


# 내가 작성한 답안
# n행 만큼 행렬 만들기(공백으로 원소 구분)
data = [[int(x) for x in input().split()] for _ in range(n)]

min_val = 0

for index in range(n):
    if min_val < min(data[index]):
        min_val = min(data[index])

print(min_val)


# 모범 답안
result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_val = min(data)
    result = max(result, min_val)

print(result)



#####################################################################
# 실전문제 4 (1이 될 때까지 p.99)

n, k = map(int, input().split())
count = 0

while True:
    sub = n % k
    count += sub
    n -= sub

    if n % k == 0:
        n //= k
        count += 1
    if n < k:
        count += (n - 1)
        break

print(count)
