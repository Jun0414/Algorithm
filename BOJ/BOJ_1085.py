
# 문제 1085번 직사각형에서 탈출
# Math(수학)


import sys
r = sys.stdin.readline


x, y, w, h = map(int, r().split())

dis = []
dis.append(abs(x-0))
dis.append(abs(y-0))
dis.append(abs(x-w))
dis.append(abs(y-h))

print(min(dis))





# 입력 예시
# 6 2 10 3

# 출력 예시
# 1