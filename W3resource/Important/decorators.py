def div(a,b):
    print(a/b)
def smart_div(func):
    def innerfunction(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return innerfunction

div = smart_div(div)
div(4,2)


def originalfunction(name):
    print(f"this is original function and your name is  {name}")

def namechanger(func):
    def innerfunction(name):
        name = "Malay"
        return func(name)
    return innerfunction
originalfunction = namechanger(originalfunction)
originalfunction("thakkar")