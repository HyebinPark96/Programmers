import math

def solution(a, b, n):
    
    # 교환해서 받는 병 카운팅
    cnt = 0
    
    while n // a > 0: # 더이상 나눠지지 않을 때까지 반복
        if n % a == 0:
            cnt += b * (n // a)
            n = n - (n - (n % a)) + (b * (n // a)) # 준 병 빼고, 받은 병 더하기 
        else: 
            cnt += b * (n // a)
            n = n - (n - (n % a)) + (b * (n // a)) # 준 병 빼고, 받은 병 더하기 

    return cnt
