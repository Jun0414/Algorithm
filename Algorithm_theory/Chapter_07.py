
# 예제 7-1 (순차탐색 p.187)

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print('생성할 원소 개수를 입력 후, 한 칸 띄고 찾고자하는 이름을 입력하시오.')

input_data = input().split()

n = int(input_data[0])
target = input_data[1]

print('원소 개수만큼 이름을 한칸 띄어쓰기 단위로 적으시오.')
name_data = list(map(str, input().split()))

print(sequential_search(n, target, name_data))



#####################################################################
# 예제 7-2 (이진탐색 p.189)

# 재귀적 표현
def recursive_binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return recursive_binary_search(array, target, mid + 1, end)
    else:
        return recursive_binary_search(array, target, start, mid - 1)


# 반복적 표현
def iterable_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target == array[mid]:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return None

n, target = map(int, input().split())
data = list(map(int, input().split()))

result1 = recursive_binary_search(data, target, 0, n - 1)
result2 = iterable_binary_search(data, target, 0, n - 1)

if result1 == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result1 + 1)

if result2 == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result2 + 1)



