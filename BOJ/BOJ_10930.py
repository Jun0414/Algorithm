
# 문제 10930번 SHA-256
# Hashing(해싱)

import sys
import hashlib
r = sys.stdin.readline

s = r().strip()
encode_s = s.encode()
hash_s = hashlib.sha256(encode_s).hexdigest()
print(hash_s)




# 입력 예시
# Baekjoon

# 출력 예시
# 9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857