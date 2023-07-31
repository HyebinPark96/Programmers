import math

def solution(a, b, n):
    
    # 교환해서 받는 병 카운팅
    cnt = 0
    
    while n // a > 0: # 더이상 나눠지지 않을 때까지 반복
        cnt += b * (n // a)
        n = (n % a) + (b * (n // a)) # 주고 남는 병 + 받을 병  

    return cnt
