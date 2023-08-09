def solution(babbling):
    str_array = ["aya", "ye", "woo", "ma"]
    repeats_str_array = ["ayaaya", "yeye", "woowoo", "mama"]
    
    answer = 0
    
    global before_len
    before_len = 0

    for i in range(len(babbling)):
        for j in range(len(str_array)):
            babbling[i] = babbling[i].replace(repeats_str_array[j], 'X')            
            babbling[i] = babbling[i].replace(str_array[j], 'O')

            if babbling[i].replace('O', '') == '':
                answer += 1
                break   

    return answer