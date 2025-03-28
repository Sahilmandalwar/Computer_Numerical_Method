a = 0
b = 3
n = 6
h = (b - a) / n

def function(x):
    return (1 + x**2) ** (-1)

first_component = function(a) + function(b)

non_three_multiple = 0
three_multiple = 0

i = a + h

while i < b:
    non_three_multiple += (function(i) + function(i+h))
    three_multiple += (function(i + 2*h))
    i += 3*h

simphson_sum = (first_component + 3 * (non_three_multiple) + 2 * (three_multiple)) * 3 * h / 8

print(simphson_sum)

