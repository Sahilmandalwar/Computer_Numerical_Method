a = 0
b = 3
n = 6
h = (b - a) / n

def function(x):
    return (1 + x**2) ** (-1)

first_component = function(a) + function(b)

odd_component = 0
even_component = 0

i = a + h

while i < b:
    odd_component += function(i)
    even_component += function(i + h)
    i += 2*h

simphson_sum = (first_component + 4 * (odd_component) + 2 * (even_component)) * h / 3

print(simphson_sum)



