n = eval(input("Enter the number of entries: "))

# def function(x):
#     return x**2 + 5*x + 6

def get_constant(valueForX):          #x coordinate for which value to be find
    numerator = query_table[valueForX]
    denominator = 1
    for key in query_table.keys():
        if key == valueForX:
            continue
        denominator *= (valueForX - key)
    return numerator / denominator 

def get_value(valueForX, variable):
    product = 1
    for key in query_table.keys():
        if key == valueForX:
            continue
        product *= (variable - key)

    return product 


query_table = {}

for i in range(n):
    x_value = eval(input(f"Enter the x{i}: "))
    y_value = eval(input(f"Enter the y{i}: "))
    # y_value = function(x_value)
    query_table[x_value] = y_value

findFor = eval(input("Enter the entry for which value to be interpolated: "))

sum = 0
for key in query_table.keys():
    sum += (get_constant(key)* get_value(key,findFor))

print(sum)



