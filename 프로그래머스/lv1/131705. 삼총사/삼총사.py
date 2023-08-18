from itertools import combinations 
def solution(number):
    answer = 0
    
    tmp_sum = 0
    combinations_list = []
    
    for i in combinations(number, 3): 
        print(list(i))
        combinations_list = list(i)
        for j in range(len(combinations_list)):
            tmp_sum += combinations_list[j]
        if tmp_sum == 0:
            answer += 1
        tmp_sum = 0
            
    return answer