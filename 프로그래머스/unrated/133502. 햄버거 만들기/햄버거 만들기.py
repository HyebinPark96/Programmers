def solution(ingredient):
    
    # !! 햄버거가 만들어져서 해당 요소들이 리스트에서 빠지더라도 반복문에서 Index out of range 오류나지 않아야 함.
    
    # 햄버거 개수
    hamburger = 0
    
    # 햄버거 재료 배열 
    hamburger_arr = []
    
    for i in ingredient:
        hamburger_arr.append(i)  
        
        # 반복문 돌면서 조회 
        # 파이썬은 slice 시 범위 벗어나도 Error 안나고 빈값 리턴 (일부만 범위에 속한다면 그 요소들만 리턴)
        if hamburger_arr[-4:] == [1,2,3,1]: # 뒤에서부터 4번째 요소 ~ 끝 요소
            
            hamburger += 1
                        
            # del 함수 사용하여 만들어진 햄버거 재료 요소들 빼내기 
            del hamburger_arr[-4:]
            
    return hamburger