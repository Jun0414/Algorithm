# O(nlogn) 정렬 : 퀵 정렬(quick sort), 병합 정렬(merge sort), 힙 정렬(heap sort)

# 퀵 정렬
def quick_sort(data):
    # 데이터가 1개 이하라면 그대로 반환
    if len(data) <= 1:
        return data

    # 피봇 및 분류할 빈 리스트 선언 (/ : 실수 나누기, // : 나눈 몫)
    pivot = data[len(data) // 2]
    lesser_data, equal_data, greater_data = [], [], []

    # 피봇을 기준으로 크고 작은 값 나누기
    for num in data:
        if num < pivot:
            lesser_data.append(num)
        elif num > pivot:
            greater_data.append(num)
        else:
            equal_data.append(num)

    # 피봇으로 쓰인 배열은 다시 호출할 필요가 없으므로 작은 것과 큰 것에서만 재분류를 위해 재귀적으로 호출
    return quick_sort(lesser_data) + equal_data + quick_sort(greater_data)

# 몇개 입력받을 것인지, 빈 리스트 선언
n = int(input())
data = []

# n개만큼 입력받기
for i in range(n):
    data.append(int(input()))

data = quick_sort(data)

# 정렬된것 출력하기
for i in range(n):
    print(data[i])
