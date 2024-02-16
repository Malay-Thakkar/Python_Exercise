def factorial(num):
    n = 1
    result = 1
    while n <= num:
        result *= n
        yield result
        n += 1
        
for value in factorial(5):
    print(value)
    
#===========================================
    
def fibonacci_generator(limit=10):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator function
for value in fibonacci_generator(9):
    print(value)
