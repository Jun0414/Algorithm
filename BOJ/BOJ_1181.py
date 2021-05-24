
# 문제 1181번 단어 정렬
# Sorting(정렬), String(문자열)


import sys
r = sys.stdin.readline

n = int(r())

words = dict()
for _ in range(n):
  word = r().strip()
  words[word] = len(word)

# 단어의 길이 순으로 먼저 정렬 후, 사전 순으로 재정렬
words = dict(sorted(words.items(), key=lambda x: (x[1], x[0])))
for word, index in words.items():
  print(word)





# 입력 예시
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

# 출력 예시
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate