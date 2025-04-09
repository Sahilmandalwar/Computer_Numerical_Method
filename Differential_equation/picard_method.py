from sympy import symbols, integrate

x,y = symbols('x y')

n = eval(input("Number of itteration: "))

initial_x = 0
initial_y = 0


'''
dy/dx = x + y
'''
function = x**2 + y**2

'''
dy/dx = f(x,y)
y = initial_y + integral(f(x,y))| x , x0
'''
new_y = initial_y
for i in range(n):
    new_y = initial_y + integrate(function.subs(y, new_y) , (x,initial_x , x))

print(new_y)

print(float(new_y.subs(x,0.4)))

