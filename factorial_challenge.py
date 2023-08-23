# Returns the value of factorial of num if it is defined otherwise returns None

def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * factorial(num - 1)
    
    # To comment multiple line selec the lines you want to comment and press ctrl+/
    # i = 0
    # f = 1
    # while i < num:
    #     i = i + 1
    #     f = f * i

    # return f


    