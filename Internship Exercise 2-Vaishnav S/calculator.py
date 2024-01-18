def add(a, b):
        return a+b
def subtract(a, b):
        return a - b
def multiply(a, b):
        return a * b
def division(a, b):
        if b==0:
                raise ValueError("Not divisible")
        return a/b
def mod(a, b):
        if b==0:
                raise ValueError("Not divisible")
        return a%b
