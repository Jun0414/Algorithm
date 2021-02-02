
# 예제 8-1 (피보나치 함수 p.210)

# 일반 재귀적 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))


# 다이나믹 프로그래밍(탑다운) 재귀적 구현

# 한번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def d_fibo(x):
    # 호출함수 확인
    print('f(' + str(x) + ')', end=' ')

    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 한번 계산했던 문제
    if d[x] != 0:
        return d[x]

    # 처음 계산하는 문제
    d[x] = d_fibo(x - 1) + d_fibo(x - 2)

    # 결과값 반환
    return d[x]

print(d_fibo(99))


# 다이나믹 프로그래밍 반복적 구현
d = [0] * 100

# 첫번째, 두번째는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])



#####################################################################
# 실전문제 2 (1로 만들기 p.217)

n = int(input())
cnt = 0

while n > 1:
    if n >= 5:
        if n % 5 == 0:
            n //= 5
            cnt += 1
        else:
            sub = n % 5
            for i in range(sub):
                n -= 1
                cnt += 1
    elif n >= 3:
        if n % 3 == 0:
            n //= 3
            cnt += 1
        else:
            sub = n % 3
            for i in range(sub):
                n -= 1
                cnt += 1
    elif n >= 2:
        if n % 2 == 0:
            n //= 2
            cnt += 1
        else:
            sub = n % 2
            for i in range(sub):
                n -= 1
                cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)


# 모범 답안
x = int(input())

# 계산된 결과 저장을 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(버틈업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

# 입력 예시
# 26



#####################################################################
# 실전문제 3 (개미 전사 p.220)

get = [0] * 101

n = int(input())
data = list(map(int, input().split()))

get[0] = data[0]
# 0번째가 더 크다면 1번째 값을 선택안하고 0번째와 더한 값을 주어야 하므로 (그 이후는 양쪽의 값과 가운데 값을 비교하여 큰 값 선택)
get[1] = max(data[0], data[1])

# get[i - 2] + data[i]의 값이 큰 값이라면 한칸 띄어진 간격이 큰 것이고, get[i - 1]의 값이 크다면 2칸이상 띄었던 값이 큰 값
for i in range(2, n):
    get[i] = max(get[i - 1], get[i - 2] + data[i])

print(get[n - 1])

# 입력 예시
# 4
# 1 3 1 5



#####################################################################
# 실전문제 4 (바닥 공사 p.223)

n = int(input())

data = [0] * 1001

data[1] = 1
data[2] = 3

for i in range(3, n + 1):
    data[i] = data[i - 1] * (data[i - 2] * 2) % 796796

print(data[n])

# 입력 예시
# 3



#####################################################################
# 실전문제 5 (효율적인 화폐 구성 p.226)
import sys

n, m = map(int, input().split())

units = []
for i in range(n):
    units.append(int(input()))


# 내가 작성한 답안

# 메모이제이션 할 리스트
data = [10001] * (m + 1)
data[0] = 0

for unit in units:
    for i in range(1, m + 1):
        if unit == i:
            data[i] = 1

        if i - unit > -1 and data[i - unit] != 10001:
            data[i] = min(data[i], data[i - unit] + 1)

if data[m] != 10001:
    print(data[m])
else:
    print(-1)


# 모범 답안

data = [10001] * (m + 1)
data[0] = 0

# 다이나믹 프로그래밍 (버틈업)
for i in range(n):
    for j in range(units[i], m + 1):
        if data[j - units[i]] != 10001:
            data[j] = min(data[j], data[j - units[i]] + 1)

if data[m] == 10001:
    print(-1)
else:
    print(data[m])

# 입력 예시
# 1)
# 2 15
# 2
# 3
# 2)
# 3 4
# 3
# 5
# 7