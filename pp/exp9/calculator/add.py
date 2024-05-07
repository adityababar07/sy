# add

# Function to add multiple numbers to a result
def add(result, *args):
    for i in args:
        result += i   
    return result
