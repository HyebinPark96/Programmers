def solution(n):
    answer = 0
    
    array = []
    
    for i in range(2, n+1, 1): # 시작, 종료, 증가폭
        array.append(i) # 배열에 2부터 n까지 다 넣어주기
    
    for i in range(2, n+1, 1):
        if(i != 0): # 아직 안 없어진 배수들이라면
            for j in range(i+i, n+1, i): # i의 배수들 없애기 (자기자신을 제외한 배수만 없애는 이유는? i가 소수라면 i의 배수는 소수가 아니기 때문에.)
                array[j-2] = 0 
    
    for i in range(len(array)):
        if(array[i] != 0): 
            answer += 1
    
    return answer