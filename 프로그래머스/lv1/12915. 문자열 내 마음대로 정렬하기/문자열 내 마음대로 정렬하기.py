def solution(strings, n):
    answer = []
    
    # 문자열의 인덱스 n번째 글자 추출 
    target_alphabet = []

    for target in strings:
        target_alphabet.append(target[n])
        
    # 오름차순 정렬
    target_alphabet.sort()
    # 사전순으로 앞선 문자열이 앞쪽에 위치하도록 복사해둔 문자열 배열 오름차순 미리 정렬해두기
    strings.sort()
    
    for alphabet in target_alphabet:
        for string in strings:
            if alphabet == string[n]:
                answer.append(string)
                strings.remove(string)
                break

    return answer
