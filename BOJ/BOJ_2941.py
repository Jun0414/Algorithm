
# 문제 2941번 크로아티아 알파벳
# 

import sys
r = sys.stdin.readline

words = r().strip()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
# 크로아티아 알파벳 카운트하고 공백으로 바꾸기
for i in range(8):
  if alphabet[i] in words:
    cnt += words.count(alphabet[i])
    words = words.replace(alphabet[i], ' ')

# 공백을 제외한 문자 카운트
for i in words:
  if i != ' ':
    cnt += 1

print(cnt)





# 입력 예시
# ljes=njak

# ddz=z=

# nljj

# c=c=


# 출력 예시
# 6

# 3

# 3

# 2