# 1. Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs. 
# Example:

# @is_admin
# def show_customer_receipt(user_type: str):
#     # Some very dangerous operation

# show_customer_receipt(user_type='user')
# > ValueError: Permission denied

# show_customer_receipt(user_type='admin')
# > function pass as it should be

def decorator(func_check_perm):
    def wrapper(*args, **kwargs):
        user_type = input('Enter your role ') #asking user for his role: user or admin
        if user_type == "admin":
            func_check_perm(*args, **kwargs)
        else:
            print("You do not have permision")
    return wrapper

def func_for_spec_permision():
    print ("You can call this function ")

Check_permision = decorator(func_for_spec_permision)

Check_permision()


# 2. Write a decorator that wraps a function in a try-except block and prints an error if any type of error has happened. Example:

# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])

# some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

# some_function_with_risky_operation({'key': 'bar'})
# > bar

operations = {
    "p": "print",
    "c": "copy",
    "i": "insert",
    "d":"delete",
}

def decorator2(operations):
    def wrapper2(key_type):
        try:
            key_type = input('Enter a Key ') #asking user for a Key in Operations
            operation = operations[key_type]
            print(f'{key_type} = {operation}')
        except KeyError:
            print(f'An error occured with "{key_type}", print the correct Key')
    return wrapper2

function = decorator2(operations)
function('p')