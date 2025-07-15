def is_prime_number(n):
    if n == 1:
        return False
    if n == 2:
        return True
    
    divisor=2
    while divisor < n-1:
        if n % divisor == 0:
            return False
        
        divisor = divisor + 1
        
    
    return True  

print(is_prime_number(58685878586858585878596959696969696969698786878696968868668659549595959495969596959599594959405906595969596930593950494959.394930493040304030040404030004040403030020202030404040404004040400404040404040404040504040303040440404040))
