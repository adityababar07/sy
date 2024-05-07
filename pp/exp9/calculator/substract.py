# substract

# Function to subtract multiple numbers from a result
def substract(result, *args):
    for i in args:
        result -= i   
    return result
