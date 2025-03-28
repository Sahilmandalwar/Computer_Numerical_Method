import math
def function(value):
    return value **2 - 30


ERROR = 1e-9

def secant_method(neg, pos, max_iter = 100):
    
    while max_iter:

        if function(pos) == function(neg) :
            return "Can't found the value"
        value = (neg * function(pos) - pos * function(neg)) / (function(pos) - function(neg))
        function_value = function(value)

        print(100 - max_iter,"--->", value)

        if abs(function_value) < ERROR:
            return value
        
        neg , pos = pos, value

        max_iter -= 1

    return "Value not found"
    
   
secant_method(5,6)


value = 5.477225
print(value**2 - 30)

    
    


