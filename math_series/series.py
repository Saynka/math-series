
# fibonnaci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
# lucas
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

# Sum-Series
def sum_series(n,a = 0,b = 1):
    for i in range(n):
        a, b = b, a + b 
    return a