def use_function(x,y,function):
    return f"The function {function.__name__} of {x} and {y} is: {function(x,y)}"

def exponent(x,y):
    return x ** y

print(use_function(10, 20, max))
print(use_function(10, 20, min))
print(use_function(2, 3, exponent))
    