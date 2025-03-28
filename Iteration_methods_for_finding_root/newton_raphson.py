import math
def derivative(value):
    return (value)*(2)

def function(value):
    return (value)**(2) - 1/14

ERROR = 1e-4

def newton_raphson(value, max_iter = 100):
    last_value = 0
    while max_iter:
        
        if(derivative(value) == 0):
            return "Value not possible"

        if abs(value - last_value) < ERROR:
            return value
        print(100 - max_iter,"--->",value)
        last_value = value
        value = value - function(value)/derivative(value)

        max_iter -= 1

    return "Value not found"

print(newton_raphson(0.2))
        