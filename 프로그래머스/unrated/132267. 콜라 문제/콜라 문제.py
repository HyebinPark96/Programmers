import math

def solution(a, b, n):
    
    # 빈 병 카운팅
    cnt = 0
    
    # 안나눠지는 병 카운팅 (한꺼번에 모아서 가장 마지막에 나눌 것)
    tmp = 0
    
    while n // a > 0: # 더이상 나눠지지 않을 때까지 반복
        if n % a == 0:
            cnt += b * (n // a)
            n = n - (n - (n % a)) + (b * (n // a)) # 준 병 빼고, 받은 병 더하기 
        else: 
            cnt += b * (n // a)
            tmp += math.floor(n % a) # 나머지는 모아두기
            n = n - (n - (n % a)) + (b * (n // a)) # 준 병 빼고, 받은 병 더하기 

    tmp_sum = cnt + tmp
    if tmp_sum >= a:
        if tmp_sum % a == 0:        
            cnt += b * (tmp_sum // a)

    
    return cnt