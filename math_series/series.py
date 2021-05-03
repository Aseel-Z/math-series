def fibonacci(n):
    """
    for any given number(index) return the corresponding value in the fibonacci series list
    [0, 1, 1, 2, 3, 5, 8, 13, ...]

    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

    

def lucas(n):
    """
    for any given number(index) return the corresponding value in the lucas series list 
    [2, 1, 3, 4, 7, 11, 18, 29, ...]

    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1) + lucas(n-2)
   
def sum_series(n, l = 0, c = 1):
    """
    a function with 1 required and 2 optional arguments that would produce an  element in the lucas/fibonacci/other series 
    The number produced depends on the value of the optional arguments if (0,1) will produce the number from the fibonacci series and if (2,1) will produce the number from the lucas series 
    """
 
    if l == 0 and c == 1:
        return fibonacci(n)
    elif  l == 2 and c == 1:
        return lucas(n)
    else:
        return n - 1 + n - 2
    

   