a = 0
b = 6
n = 6
h = (b - a) / n

def function(x):
    return (1 + x**2) ** (-1)

first_component = function(a) + function(b)

second_component = 0

i = a + h

while i < b:
    second_component += function(i)
    i += h


trapezoidal_sum = (first_component + 2 * second_component) * h / 2

print(trapezoidal_sum)