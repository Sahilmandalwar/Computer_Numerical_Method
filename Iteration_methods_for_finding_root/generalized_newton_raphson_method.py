def function(x):
    return x**3 - x**2 - x + 1

def derivative(x):
    return 3*x**2 - 2*x - 1

accuracy = 1e-8

def newton_raphson_method(initial_approximation,m):
    if derivative(initial_approximation) == 0:
        raise ValueError(f"{initial_approximation} will divert the solution.")
    maxIter = 100

    for i in range(maxIter):
        denominator = derivative(initial_approximation)
        if denominator == 0:
            raise ValueError("initial approximation is not leading any solution.")
        new_x = initial_approximation - m*function(initial_approximation) / denominator
        if(abs(new_x - initial_approximation) < accuracy):
            return new_x

        initial_approximation = new_x
    return new_x

print(newton_raphson_method(0.9,1))
