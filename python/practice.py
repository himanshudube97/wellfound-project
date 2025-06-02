# create a calculator project


def add_numbers(*args):
    sum = 0
    for x in args:
        sum = sum + x
    return sum

sum_result = add_numbers(2, 3,4 ,5)
print(sum_result)


def add_two_numbers(num1:int, num2: int):

    
    sum = int(num1) + int(num2)
    return sum 

def subtract_two_numbers(num1: int, num2: int):

    
    difference = int(num1) - int(num2) if int(num1) > int(num2) else int(num2) - int(num1)
    return difference

def multiply_two_numbers(num1: int, num2: int):

    
    product  =  int(num1)  * int(num2)
    return product

def divide_two_numbers(num1: int, num2: int):
    
    if num2 == 0: return "Cannot divide by zero"

    qotient = int(num1) / int(num2)
    return qotient


def Calculator(a:int, b:int, operation:str):
    if a == None or b == None:
        return "Please enter a valid number"
    
    result = 0
    if(operation == "+"):
        result  = add_two_numbers(a,b)
    elif operation == "-":
        result = subtract_two_numbers(a, b)
    elif operation == "*":
        result = multiply_two_numbers(a,b)
    elif operation == "/":
        result = divide_two_numbers(a, b)

    return result

def take_input_and_calculate_and_print():
    inp1 = input("Enter the first number")
    inp2 = input("Enter the second number")
    operation = input("Enter the operation")

    result = Calculator(inp1, inp2, operation)
    print(result)
    return

take_input_and_calculate_and_print()



## second Working something with dictionary. 

details = {
    "name": "Himanshu",
    "age": 20
}