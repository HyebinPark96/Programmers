def solution(t, p):
    # 문자열 p 길이 
    len_p = len(p)
    
    arr = []
    # t를 p만큼씩 잘라서 배열에 넣기 
    for i in range(len(t)):
        if i <= len(t) - len_p: 
            arr.append(int(t[i:i+len_p]))

    print(arr)
    answer = 0
    
    for num in arr:
        if num <= int(p):
            answer += 1    
    
    return answer