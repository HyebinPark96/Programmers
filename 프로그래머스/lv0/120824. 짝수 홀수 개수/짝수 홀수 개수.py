def solution(num_list):
    answer = []
    
    evenCnt = 0
    oddCnt = 0
    
    for target in num_list: 
        if(target % 2 == 0): # 짝수
            evenCnt += 1
        else: # 홀수
            oddCnt += 1
            
    answer.append(evenCnt)
    answer.append(oddCnt)
    
    return answer