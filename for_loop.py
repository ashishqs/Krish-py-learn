def get_total(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total
    
number = [1, 2, 3, 4, 5]
print(get_total(number))


n2 = range(1,989789)
print(get_total(n2))

# for i in range(0, 101, 10):
#     print(i)
    
# for i in range(0, 101, 3):
#     print(i)