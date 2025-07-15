def sum_up_to(count):
    sum = 0
    n = 0

    while n < count:
        n = n + 1
        sum = sum + n
    
    return sum
    






print(f"{sum_up_to(5)}")
print(f"{sum_up_to(10)}")