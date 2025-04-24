n = int(input("Enter the Number of Entries: "))

def get_term(p,i):
    return (p + (i - 1)) / i

def newton_backward_difference(diff_array, p, n):
    sum = diff_array[n-1][0]
    aux_product = 1
    for i in range(1, n):
        aux_product *= get_term(p,i)
        sum += (aux_product * diff_array[n-1][i])
    return sum

    

data = {}

for i in range(n):
    x_value = int(input("Enter the x values: "))
    y_value = int(input("Enter the y values: "))
    data[x_value] = y_value


for i in range(n):
    data[x[i]] = y[i]
 

dict_list = list(data.items())
findFirstTwo = dict_list[:2]

h = findFirstTwo[1][0] - findFirstTwo[0][0]

m = float(input("Enter the entry whose interpolated value to find: "))

p = (m - dict_list[n-1][0]) / h

y_values_in_data = [value for value in data.values()]

diff_array = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    diff_array[i][0] = y_values_in_data[i]

for j in range(1,n):
    for i in range(n-1, j - 1, -1):
        diff_array[i][j] = diff_array[i][j-1] - diff_array[i-1][j-1]

print(newton_backward_difference(diff_array, p, n))


