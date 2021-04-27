
# 문제 1920번 수 찾기
# Binary Search(이진 탐색)


# 재귀적 이진 탐색 알고리즘(binary_search_recursion)
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = int((start + end) / 2)
    # print(mid, "mid")

    if (data[mid] == target): return data[mid]
    elif (data[mid] > target): end = mid - 1
    else: start = mid + 1

    return binary_search_recursion(target, start, end, data)


n = int(input())
data = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

data.sort()
start = 0
end = len(data) - 1
# print(data)

for i in range(m):
    # print(target[i], "num")
    flag = binary_search_recursion(target[i], start, end, data)
    # print(flag, "flag")

    if (flag == target[i]): print(1)
    else: print(0)


# 이진탐색 알고리즘(binary_search)
# def binary_search(target, data):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target: return data[mid]
#         elif data[mid] < target: start = mid + 1
#         else: end = mid -1
#
#     return None






# 입력 예시
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 출력 예시
# 1
# 1
# 0
# 0
# 1