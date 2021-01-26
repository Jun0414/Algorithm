
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



#####################################################################
# 예제 6-6 (계수정렬 p.174)

# 모든 원소의 값이 0보다 크거나 같은 조건
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 생성
count = [0] * (max(array) + 1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

# count 개수 만큼 데이터 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')



#####################################################################
# 예제 6-7 (파이썬 정렬 라이브러리 p.176)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted() 반환 결과는 리스트
result = sorted(array)
print(result)

# sort() 반환 결과는 리스트 (별도의 리스트를 만들지 않고 내부에서 정렬)
array.sort()
print(array)

# key값을 활용한 정렬 (setting에서 반환하는 인덱스 값이 key로 설정됨)
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)



#####################################################################
# 실전문제 2 (위에서 아래로 p.178)

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for i in data:
    print(i, end=' ')

# 입력 예시
# 3
# 15
# 27
# 12



#####################################################################
# 실전문제 3 (성적이 낮은 순서로 학생 출력하기 p.180)

n = int(input())

data = []
for i in range(n):
    input_data = input().split()

    # dictionary처럼 쓰기위해서 append()안에 ()를 만들어 거기에 리스트처럼 넣어주는 구조
    data.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]

# setting의 설정을 이용한 표현
data = sorted(data, key=setting)

# 람다로 표현
data = sorted(data, key=lambda score: score[1])

# 이름만 출력
for student in data:
    print(student[0], end=' ')

# 입력 예시
# 2
# 홍길동 95
# 이순신 77



#####################################################################
# 실전문제 4 (두 배열의 원소 교체 p.182)

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 내가 작성한 답안

# 계수정렬 함수
def count_sort(data):
    array = [0] * (max(data) + 1)
    p = 0

    for i in range(len(data)):
        array[data[i]] += 1

    for i in range(len(array)):
        for j in range(array[i]):
            data[p] = i
            p += 1

count_sort(A)
count_sort(B)

# A는 앞에서부터 B는 뒤에서부터 교체
for i in range(k):
    if A[i] < B[n - i - 1]:
        A[i], B[n - i - 1] = B[n - i - 1], A[i]

print(sum(A))


# 모범 답안

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

# 입력 예시
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
