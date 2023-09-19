# 풀이 설계
# 1) num가 팰린드롬 수 인지 판단하는 함수 하나를 먼저 만든다.
# 2) 에라토스테네스의 체 알고리즘 함수를 하나 만든다.
# 3) 적절한 max값을 잡고 에라토스테네스의 체를 수행한 후 팰린드롬 수 인지 검사한다.
import math

def palindrome(num):
    num_str = str(num)
    for ch_re, ch in zip(reversed(num_str), num_str):
        if ch != ch_re:
            return False
    return True

def eratos(n, m_n):
    origin_n = n
    n = m_n
    eratos_table = [True for _ in range(n)]

    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if eratos_table[i] == True:
            for j in range(i+i, n, i):
                eratos_table[j] = False
    
    return [i for i in range(origin_n,n) if eratos_table[i] == True]

if __name__ == "__main__":

    N = int(input())
    N = 2 if N == 1 else N
    max_n = N*2+10000 if N < 98689 else 1003002 # 적절한 max설정

    prime_num = eratos(N, max_n)
    for num in prime_num:
        if palindrome(num) == True:
            print(num)
            break
