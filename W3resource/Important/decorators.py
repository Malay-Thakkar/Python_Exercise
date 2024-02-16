# def div(a,b):
#     print(a/b)
# def smart_div(func):
#     def innerfunction(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return innerfunction

# div = smart_div(div)
# div(4,2)


# def originalfunction(name):
#     print(f"this is original function and your name is  {name}")

# def namechanger(func):
#     def innerfunction(name):
#         name = "Malay"
#         return func(name)
#     return innerfunction
# originalfunction = namechanger(originalfunction)
# originalfunction("thakkar")
#========================================================================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def decorater(func):
    def innerfunction(n):
        if n >= 0:
            return func(n)
        else:
            return ValueError("N can not be negative")  
    return innerfunction

factorial = decorater(factorial)
print(factorial(5))

#============================
def decoraterfunc(func):
    def wrapper(n):
        if n <= 0:
            return ValueError("N can not be negative or zero")
        else:
            return func(n)
    return wrapper

@decoraterfunc
def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial2(-10))

