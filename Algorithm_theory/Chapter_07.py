
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



#####################################################################
# 이진탐색 트리 구현

# 노드 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 재귀적 구현
class RecursiveBinarySearchTree(Node):
    def __init__(self, root):
        self.root = root
    # 노드 삽입
    def insert(self, data):
        self.root = self._insert_value(self.root, data)

        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    # 노드 탐색
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)

        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False

        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True

            # 삭제할 노드가 자식이 2개일 경우
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾아서 교체
                parent, child = node, node.right

                while child.left is not None:
                    parent, child = child, child.left

                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right

                node = child

            # 자식 노드가 1개일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)

        return node, deleted

# 이진탐색 트리에 삽입, 삭제 및 출력
arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = Node(30)
bst = RecursiveBinarySearchTree(root)
for i in arr:
    bst.insert(i)

print(bst.find(22)) # True
print(bst.find(61)) # False
print(bst.find(60)) # True
print(bst.delete(60)) # True
print(bst.find(60)) # False
print(bst.delete(22)) # True
print(bst.delete(44)) # True
print(bst.find(22)) # False
print(bst.find(44)) # False


# 단순 구현
class BinarySearchTree(Node):
    def __init__(self, root):
        self.root = root

    # 노드 삽입
    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 노드 탐색
    def find(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    # 노드 삭제
    def delete(self, value):
        # 삭제할 노드가 있는지 검사하고 없으면 False리턴
        # 검사를 한 후에는 삭제할 노드가 current_node, 삭제할 노드의 부모 노드가 parent가 된다.
        is_search = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if is_search == False:
            return False

        # 삭제할 노드가 자식 노드를 갖고 있지 않을 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        # 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

                # 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None

            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

        return True

# 이진탐색 트리에 삽입, 삭제 및 출력
arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = Node(30)
bst = BinarySearchTree(root)
for i in arr:
    bst.insert(i)

print(bst.find(22)) # True
print(bst.find(61)) # False
print(bst.find(60)) # True
print(bst.delete(60)) # True
print(bst.find(60)) # False
print(bst.delete(22)) # True
print(bst.delete(44)) # True
print(bst.find(22)) # False
print(bst.find(44)) # False



#####################################################################
# 예제 7-4 (빠르게 한 줄 입력받기 p.196)
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)

# 입력 예시
# Hello, Coding Test!



#####################################################################
# 실전문제 2 (부품 찾기 p.197)

# 이진 탐색
n = int(input())
data_N = list(map(int, input().split()))
m = int(input())
data_M = list(map(int, input().split()))

data_N.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in data_M:
    if binary_search(data_N, i, 0, n - 1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 계수 정렬
n = int(input())
array = [0] * 1000001

# 가게에 있는 부품 카운트
for i in input().split():
    array[i] = 1

m = int(input())
data_M = list(map(int, input().split()))

# 부품 존재여부 확인
for i in data_M:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


# 집합 자료형(한번만 등장했는지를 판단할때는 유용하다)
n = int(input())
array = set(map(int, input().split()))
m = int(input())
data_M = list(map(int, input().split()))

for i in data_M:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9



#####################################################################
# 실전문제 3 (떡볶이 떡 만들기 p.201)

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in array:
            if i > mid:
                total += i - mid

        if total == target:
            return mid
        elif total < target:
            end = mid - 1
        else:
            enough = mid
            start = mid + 1
    return enough

print(binary_search(rice_cake, m, 0, max(rice_cake)))

# 입력 예시
# 4 6
# 19 15 10 17
