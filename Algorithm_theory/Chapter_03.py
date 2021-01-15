
# # 예제 3-1 (거스름돈 p.87)
# # 그리디 -> 다이나믹 프로그래밍 or 그래프
#
# change = 1260
# count = 0
# coin_type = [500, 100, 50, 10]  #왜 {}로하면 14가 뜨고, []로하면 6이 뜨지..?
#
# for coin in coin_type:
#     count += change // coin
#     change %= coin
#
# print(count)


#####################################################################
# # 실전문제 2 (큰 수의 법칙 p.92)
# # 가장 큰 수와 두번째 큰 수만 활용
#
# # 공백 구분으로 입력 받기
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
# num = data[0]
#
#
# # 내가 작성한 답안
# sum = 0
# _k = k
#
# for _ in range(m):
#     if num <= data[0] and _k != 0:
#         num = data[0]
#         _k -= 1
#     if _k == 0:
#         num = data[1]
#         _k = 3
#     sum += num
#
# print(sum)
#
#
# # 효율적인 답안
# sum = 0
#
# # 가장 큰 수가 더해지는 횟수
# count = int(m / (k + 1)) * k
# # 딱 나누어 떨어지지 않았을 경우 그 만큼 큰 수를 더해주기위해
# count += m % (k + 1)
#
# sum += (count) * data[0]
# sum += (m - count) * data[1]
#
# print(sum)

