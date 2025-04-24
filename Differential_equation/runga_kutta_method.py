'''
x = 0, y = 1
x = 0.2, y = ?

dy/dx = x + y
'''

def function(x,y):
    return y - x**2 + 1

x0 = 0
y0 = 0.5

x1 = 0.2

h = x1 - x0

k1 = h * (function(x0, y0))
k2 = h * (function(x0 + h / 2, y0 + k1/ 2))
k3 = h * (function(x0 + h / 2, y0 + k2/ 2))
k4 = h * (function(x0 + h, y0 + k3))

k = (k1 + 2*k2 + 2*k3 + k4) / 6

y1 = y0 + k

print(y1)