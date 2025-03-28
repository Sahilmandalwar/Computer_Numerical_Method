
import math
def function(value):

   
    return value**2 - 2

ERROR = 1e-4

def bisection_method(neg, pos):
    iteration = math.floor(math.log2(pos - neg) - math.log2(ERROR))

    while iteration:
        mid = (neg + pos) / 2
        
        function_value = function(mid)
        if function_value < 0:
            neg = mid
        elif function_value > 0:
            pos = mid
        else:
            break

        print(mid)
        iteration -= 1
    
    return mid

print(bisection_method(1.414,1.415))

    