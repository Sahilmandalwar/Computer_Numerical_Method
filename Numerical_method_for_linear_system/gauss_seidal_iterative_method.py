
maxIter = 100
tol = 1e-10

def gauss_jacobi_method(coefficient_variable,maxIter):
    global tol
    initial_x = 0
    initial_y = 0
    initial_z = 0

    for i in range(maxIter):
        new_x = (coefficient_variable[0][3] - coefficient_variable[0][1] * initial_y - coefficient_variable[0][2] * initial_z) / coefficient_variable[0][0]
        new_y = (coefficient_variable[1][3] - coefficient_variable[1][0] * initial_x - coefficient_variable[1][2] * initial_z) / coefficient_variable[1][1]
        new_z = (coefficient_variable[2][3] - coefficient_variable[2][0] * initial_x - coefficient_variable[2][1] * initial_y) / coefficient_variable[2][2]

        if(max(abs(new_x - initial_x), abs(new_y - initial_y), abs(new_z - initial_z)) < tol):
            return (f"{new_x:.5f},{new_y:.5f},{new_z:.5f}")
        initial_x = new_x
        initial_y = new_y
        initial_z = new_z

    return (f"{initial_x:.5f},{initial_y:.5f},{initial_z:.5f}")



# coefficient_variable = [[10,2,1,7],[1,5,1,-8],[2,3,10,6]]


coefficient_variable = [[0 for i in range(4)] for j in range(3)]
print("It is expected from the question setter the form must be diagonal dominant!")
for i in range(3):
    print(f"{i+1}th equation-")
    coefficient_variable[i][0] = int(input("Enter the coefficient of x: "))
    coefficient_variable[i][1] = int(input("Enter the coefficient of y: "))
    coefficient_variable[i][2] = int(input("Enter the coefficient of z: "))
    coefficient_variable[i][3] = int(input("Enter the constant term: "))

print(gauss_jacobi_method(coefficient_variable, maxIter))





