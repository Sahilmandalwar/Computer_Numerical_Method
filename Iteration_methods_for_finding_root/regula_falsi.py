def function(value):
    return value**2 - 2

ERROR = 1e-5

def regula_falsi(neg, pos, max_iter = 100):

    
    while max_iter:

        if function(neg) == function(pos):
            return "solution can't found in the given input"

        value = (neg * function(pos) - pos * function(neg))/(function(pos) - function(neg))
        function_value = function(value)

        print(100 - max_iter,"-->", value)

        if abs(function_value) < ERROR:
            return value
        
        if function_value > 0:
            pos = value
        else:
            neg = value

        max_iter -= 1


    return value

regula_falsi(1.4,1.5)