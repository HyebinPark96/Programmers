def solution(s):
    answer = []
    
    s_list = list(s)
    
    # 동일한 글자 찾으면 해당 위치 담는 배열
    tmp = []
    
    answer.append(-1) # 첫번째 요소는 무조건 -1
    
    for i in range(len(s_list)):
        for j in range(len(s_list)):

            if i > j: # 자신보다 앞 원소랑만 비교하기(자기 자신은 무시)
                if s_list[i] == s_list[j]: # 같은 글자 있다면
                    tmp.append(j)
            else: 
                break

            # print('j: ' + str(j))
            # print('i: ' + str(i))
            
            if j == i - 1: # 반복문 끝 직전에 조건  
                # 가장 근처 같은 값이랑만 비교하기
                # print(tmp)
                if len(tmp) > 0:
                    answer.append(i - tmp[len(tmp) - 1])
                    tmp = []
                else:
                    answer.append(-1)
                    break
                        
    return answer