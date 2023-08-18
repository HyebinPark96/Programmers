def solution(arr):
    answer = []
    
    min = arr[0]
    idx = 0
    if len(arr) > 1:
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
                idx = i

        # 가장 작은 수 제거
        del arr[idx]
        answer = arr
    else:
        answer = [-1]

    return answer