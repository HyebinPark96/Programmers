def solution(numbers):
    answer = []
    
    tmp_sum = 0
    
    # 같은 수 안 넣도록 
    # 오름차순 정렬
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if(i != j): # 자기자신 빼고 더하기
                tmp_sum += numbers[i] + numbers[j] 
                if(tmp_sum not in answer):
                    answer.append(tmp_sum)
            tmp_sum = 0
    
    answer.sort()
    
    return answer