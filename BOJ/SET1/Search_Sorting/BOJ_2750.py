
# 기초 정렬
# 문제 2750번 수 정렬하기
# Sorting(정렬)

# O(nlogn) 정렬 : 퀵 정렬(quick sort), 병합 정렬(merge sort), 힙 정렬(heap sort)


import sys
r = sys.stdin.readline

n = int(r())
input_data = list(int(r()) for _ in range(n))

input_data.sort()
for i in input_data:
    print(i)



# # 병합 정렬
# def merge_sort(data):
#     # 리스트가 2개 미만일 경우 그대로 반환
#     if len(data) < 2:
#         return data

#     # 중간 지점 저장
#     mid = len(data) // 2
#     # 중간지점을 기점으로 앞리스트와 뒤리스트 리스트 안의 인덱스가 하나가 될때까지 나누기(재귀적)
#     low_data = merge_sort(data[:mid])
#     high_data = merge_sort(data[mid:])

#     # 합칠 리스트 생성
#     merged_data = []
#     l = h = 0
#     # 두 리스트 중 하나라도 마지막 인덱스까지 먼저 도달하면 루프 탈출
#     while l < len(low_data) and h < len(high_data):
#         if low_data[l] < high_data[h]:
#             merged_data.append(low_data[l])
#             l += 1
#         else:
#             merged_data.append(high_data[h])
#             h += 1
#     # 나머지 뒤에 이어붙이기
#     merged_data += low_data[l:]
#     merged_data += high_data[h:]

#     return merged_data


# # 몇개 입력받을 것인지, 빈 리스트 선언
# n = int(input())
# data = []

# # n개만큼 입력받기
# for i in range(n):
#     data.append(int(input()))

# # list.sort(data)
# # data = quick_sort(data)
# data = merge_sort(data)

# # 정렬된것 출력하기
# for i in range(n):
#     print(data[i])


# # 퀵 정렬(기본 내장 함수: list.sort())
# def quick_sort(data):
#     # 데이터가 1개 이하라면 그대로 반환
#     if len(data) <= 1:
#         return data
#
#     # 피봇 및 분류할 빈 리스트 선언 (/ : 실수 나누기, // : 나눈 몫)
#     pivot = data[len(data) // 2]
#     lesser_data, equal_data, greater_data = [], [], []
#
#     # 피봇을 기준으로 크고 작은 값 나누기
#     for num in data:
#         if num < pivot:
#             lesser_data.append(num)
#         elif num > pivot:
#             greater_data.append(num)
#         else:
#             equal_data.append(num)
#
#     # 피봇으로 쓰인 배열은 다시 호출할 필요가 없으므로 작은 것과 큰 것에서만 재분류를 위해 재귀적으로 호출
#     return quick_sort(lesser_data) + equal_data + quick_sort(greater_data)


# # 퀵 정렬 최적화(보완이 필요함)
# def quick_sort(data):
#     # 정렬 범위를 받는 함수
#     def sort(low, high):
#         # 인덱스가 역전되면 그냥 탈출
#         if high <= low:
#             return
#
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#         return data
#
#     # 피봇 기준으로 작은값은 왼쪽, 큰값은 오른쪽으로 정렬하는 함수
#     def partition(low, high):
#         # 피봇은 인덱스의 중앙값
#         pivot = data[(low + high) // 2]
#
#         # 왼쪽에서 피봇보다 큰값 또는 오른쪽에서 피봇보다 작은값 찾아서 바꿔주기(반복)
#         while low <= high:
#             while data[low] < pivot:
#                 low += 1
#             while data[high] < pivot:
#                 high -= 1
#             if low <= high:
#                 data[low], data[high] = data[high], data[low]
#                 low, high = low + 1, high - 1
#         return low
#
#     # 배열의 시작과 끝 인덱스 반환
#     return sort(0, len(data) - 1)




# 입력 예시
# 5
# 5
# 2
# 3
# 4
# 1

# 출력 예시
# 1
# 2
# 3
# 4
# 5