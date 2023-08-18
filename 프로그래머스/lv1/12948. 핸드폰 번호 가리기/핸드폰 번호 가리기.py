def solution(phone_number):
    masking_phone_number = '';
    
    for i in range(len(phone_number)):
        print(i)
        if i < len(phone_number) - 4:
            masking_phone_number += "*"
        else:
            masking_phone_number += phone_number[i] 
            
    return masking_phone_number