import math
def function(value):
    return 5*(value + 6)/(value+5)

ERROR = 1e-4



def iteration_method(value, max_iter = 100):
    prev_value = value

    while max_iter:
        value = function(value)
        print(100 - max_iter, "--->",value)
        if abs(value - prev_value) < ERROR:
            return value
        prev_value = value

        
        max_iter -= 1

    return value

print(iteration_method(5))
