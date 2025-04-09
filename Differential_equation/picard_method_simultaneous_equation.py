n = 3

from sympy import integrate, symbols

'''
dy/dx = z
dz/dx = x**3 * (y + z)
'''

x,y,z = symbols('x y z')


y_function = x + z
z_function = x - y ** 2

x_0 = 0
y_0 = 2
z_0 = 1

new_y = y_0
new_z = z_0

for i in range(n): 
    temp_y = y_0 + integrate(y_function.subs({z : new_z, y : new_y}), (x, x_0, x))
    new_z = z_0 + integrate(z_function.subs({z : new_z , y : new_y}),  (x, x_0, x))

    new_y = temp_y
    print(f"{i + 1} iteration: ")
    print("y : ", new_y.subs({x : 0.1}))
    print("z : ", new_z.subs({x : 0.1}))
    print()




