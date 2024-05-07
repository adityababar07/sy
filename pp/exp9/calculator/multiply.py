# multiply

# Function to multiply multiple numbers with a result
def multiply(result, *args):
    for i in args:
        result *= i   
    return result
