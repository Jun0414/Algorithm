
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



