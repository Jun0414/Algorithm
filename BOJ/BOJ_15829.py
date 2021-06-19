
# 문제 15829번 Hashing
# String(문자열), Hashing(해싱)


import sys
r = sys.stdin.readline


l = int(r())
hash_str = r().strip()

sum = 0

for i in range(len(hash_str)):
  sum += (ord(hash_str[i]) - ord('a') + 1) * (31 ** i)

print(sum % 1234567891)






# 입력 예시
# 5
# abcde

# 3
# zzz

# 1 i

# 출력 예시
# 4739715

# 25818

# 9