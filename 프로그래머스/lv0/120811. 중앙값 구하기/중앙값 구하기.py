def solution(array):
    answer = 0
    
    array.sort()
    
    length = len(array)
    
    if(length % 2 == 0): #짝수
        answer = array[(length // 2) - 1] 
    else: # 홀수
        print(length)
        answer = array[(length // 2)]
        print(array[(length // 2)])
        
    return answer