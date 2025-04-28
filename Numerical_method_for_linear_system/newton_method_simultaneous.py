def function_g(x,y):
    return 2*x**2 + 3*y*x + y**2 - 3

def function_f(x,y):
    return 4*x**2 + 2*x*y + y**2 - 30

def function_gx(x,y):
    return 4*x + 3*y

def function_gy(x,y):
    return 3*x + 2*y

def function_fx(x,y):
    return 8*x + 2*y

def function_fy(x,y):
    return 2*x + 2*y

accuracy = 1e-12

def bulky_function_with_x(x,y):
    numerator = function_f(x,y) * function_gy(x,y) - function_g(x,y) * function_fy(x,y)
    denominator = function_fx(x,y) * function_gy(x,y) - function_gx(x,y) * function_fy(x,y)
    return numerator / denominator

def bulky_function_with_y(x,y):
    numerator = function_g(x,y) * function_fx(x,y) - function_f(x,y) * function_gx(x,y)
    denominator = function_fx(x,y) * function_gy(x,y) - function_gx(x,y) * function_fy(x,y)
    return numerator / denominator

def newton_raphson_simultaneou_method(initial_x, initial_y):
    maxIter = 100
    for _ in range(maxIter):
        new_x = initial_x - (bulky_function_with_x(initial_x,initial_y))
        new_y = initial_y - (bulky_function_with_y(initial_x,initial_y))

        if max(abs(new_x - initial_x) , abs(new_y - initial_y)) < accuracy:
            return (new_x, new_y)

        initial_x = new_x
        initial_y = new_y
    
    return new_x , new_y


x,y = newton_raphson_simultaneou_method(-2.4,5.8)

print(x,y)
