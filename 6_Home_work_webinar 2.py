# Task 1: Function as a Parameter
# Write a Python function called apply_operation that takes three arguments: 
#- operation: A function that takes two numeric arguments and performs a mathematical operation 
# (e.g., add, subtract, multiply, divide).
# - operand1: The first numeric operand.
# - operand2: The second numeric operand.
# The apply_operation function should return the result of applying the operation function to operand1 and operand2. 
# Test your function with at least two different operations.

o1 = int(input("1st operand: "))
o2 = int(input("2nd operand: "))
operation = input("operation (+-/*): ")

def sum(o1, o2):
    return o1 + o2

def substract(o1, o2):
    return o1 - o2

def divide(o1, o2):
    return o1 / o2

def multiply(o1, o2):
    return o1 * o2

operations = {
    "+": sum,
    "-": substract,
    "/": divide,
    "*": multiply,
    #   '**':
    #   '//':
}

def apply_operation(o1, o2, operation):
    if operation in operations.keys():
        return operations[operation](o1, o2)
    
    ("Uknown operator", operation)

result = apply_operation(o1, o2,operation)
print(result)

# Unit Test_1
a=2
b=4
res_test = apply_operation(a,b,"+")
if res_test == 6:
    print("test successful")
else:
    print("test failed")

# Unit Test_2
a=2
b=4
res_test_2 = apply_operation(a,b,"-")
if res_test_2 == -2:
    print("test successful")
else:
    print("test failed")

import time

# Unit Test_time
a=500000000
b=4
start = time.time()
res_test_3 = apply_operation(a,b,"*")
end = time.time()
delta = end - start
if res_test_3 == 2000000000 and delta <1:
    print("test 03 - success")
else:
    print("test 03 - fail")



# Task 2: Function as a Return Value
# Create a function called get_multiplier that takes a single numeric argument multiplier.
# Inside this function, define and return another function (inner function) that takes a single numeric argument number and returns the result of multiplying number by multiplier.
# Write a code snippet to demonstrate the use of get_multiplier. Use the returned function to multiply a number by different multipliers.

def get_multiplier(num):
    def another_function(n):
        return num * n
    return another_function

result_what_multiply = get_multiplier(7)
result_for_multiplying = result_what_multiply(3)
print(result_for_multiplying)



# Task 3: Function as an Element of a List
# Create a list called operation_list that contains three functions: add, subtract, and multiply.
# Each of these functions should take two numeric arguments and perform the respective operation. For example, add(3, 5) should return 8.
# Iterate through the operation_list and apply each operation to a pair of numbers. Print the results.

a1 = int(input("1st operand: "))
a2 = int(input("2nd operand: "))

def add(a1, a2):
    return a1 + a2

def substract(a1, a2):
    return a1 - a2

def multiply(a1, a2):
    return a1 * a2

operation_list = [add, substract, multiply]
for operations_2 in operation_list:
    res = operations_2 (a1, a2)
    print(res)