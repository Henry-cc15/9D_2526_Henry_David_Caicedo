# Created by:Henry David caicedo
# Group: 9D
# Date: 19 sep 2025
# Topic, problem, theme: 4 basic math operations

#Defining the function (is the process)
def math_operation_addition(num1,num2):
    """
    Displays the addition of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        addition (int): 
      """
    addition_result = num1 + num2

    return addition_result

def math_operation_subtraction(num1,num2):
    """
    Displays the subtraction of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        addition (int): 
      """
    subtraction_result = num1 - num2

    return subtraction_result

def math_operation_multiplication(num1,num2):
    """
    Displays the multiplication of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        multiplication (int): 
      """
    multiplication_result = num1 * num2

    return multiplication_result

def math_operation_division(num1,num2):
    """
    Displays the division of two numbers

    Args:
        num1 (int): first number
        num2 (int): second number
    
    Returns:
        division (int): 
      """
   
    if num2 == 0:
        print ("Error: it´s not possible to divide by zero, choose other number")
    else:
        division_result = num1 / num2

    return division_result

# Main program
# The user enters the information, calls the function and display the results

print("=== Results ===")
print()

# Get information from user
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# Calling the functions
addition_final_result = math_operation_addition(num1,num2)
subtraction_final_result = math_operation_subtraction(num1,num2)
multiplication_final_result = math_operation_multiplication(num1,num2)
division_final_result = math_operation_division(num1,num2)


print(f"\nthe addition= {addition_final_result}")
print(f"\nthe subtraction= {subtraction_final_result}")
print(f"\nth multiplication= {multiplication_final_result}")
print(f"\nthe division= {division_final_result}")
