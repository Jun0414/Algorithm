
# 예제 6-1 (선택정렬 p.159)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)



#####################################################################
# 예제 6-3 (삽입정렬 p.164)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # i부터 1까지 감소하며 반복한다 (range(start, end, step))
   for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)



#####################################################################
# 예제 6-4 (퀵정렬 p.168)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 정통 퀵정렬
def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 원소 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 원소 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 right와 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않았다면 left와 right 교체
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

print(array)


# 파이썬 전용 퀵정렬(속도는 조금 느리다)
def quick_sort_py(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [y for y in tail if y > pivot]

    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(array))
