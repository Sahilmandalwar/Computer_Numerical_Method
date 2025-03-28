n = int(input("Enter the number of entries: "))

def get_term(p, i):
    return ((p - (i - 1)) / (i))

def newton_forward_difference(diff_array,p,n):
    sum = diff_array[0][0]
    aux_product = 1
    for i in range(1,n):
        aux_product *= get_term(p, i)
        sum += (aux_product*diff_array[0][i])
    return sum

data = {}
for i in range(n):
    x_value = float(input("Enter the x value: "))
    y_value = float(input("Enter the y value: "))
    data[x_value] = y_value

findFirstTwo = list(data.items())[:2]

m = float(input("Enter the entry whose interpolated value to find: "))

h = (findFirstTwo[1][0] - findFirstTwo[0][0])
p = (m - findFirstTwo[0][0])/h

y_values_in_data = [value for value in data.values()]

diff_array = [[0 for i in range(n)] for j in range(n)]

for j in range(n):
    diff_array[j][0] = y_values_in_data[j]

for j in range(1,n):
    for i in range(n - j):
        diff_array[i][j] = diff_array[i+1][j-1] - diff_array[i][j-1]

print(newton_forward_difference(diff_array, p, n))





