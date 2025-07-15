def is_even(k):
    if k % 2 == 0:
        return True
    else:
        return False


n = 0

while n < 100:
    n = n + 1
    if is_even(n):
        print(n)
    
    
    
        