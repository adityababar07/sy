# division

# Function to divide the result by multiple numbers
def division(result, *args):
    for i in args:
        result /= i   
    return result
