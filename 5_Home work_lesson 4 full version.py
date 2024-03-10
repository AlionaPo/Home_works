#Recursive Ramblings: When Functions Meet Loops

#1. Write a function called `find_primes` that takes in two integers a and b 
#and returns a list of all the prime numbers between a and b (inclusive).
a=int(input('Enter a 1st integer: '))
b=int(input('Enter a 2nd integer: '))

def find_primes(a: int, b: int) -> list[int]:
    numbers_list = []
    for numbers in range(a, b + 1):
        if numbers > 1:
            is_prime = True
            for i in range(2, int(numbers**0.5) + 1):
                if numbers % i == 0:
                    is_prime = False
                    break
            if is_prime:
                numbers_list.append(numbers)
    return numbers_list

prime_list = find_primes(a, b)
print(prime_list)

#2. Write a function called `unique_characters` that takes in a string s and returns a Boolean value indicating whether or not all the characters in s are unique. 
#For example, the string "abcdefg" has unique characters, but the string "abcdeff" does not.

#s=input('Write a string: ')

# def unique_characters (s):
#        sorted_s=sorted(s)
#        for ltrs in range(len(sorted_s)-1):
#            if sorted_s[ltrs] == sorted_s[ltrs+1]:
#                r#eturn 'Characters not unique'
#        return 'Characters unique'
               
# print (unique_characters(s))


# s=input('Write a string: ')

# def unique_characters (s):
#     if len(set(s)) == len (s):
#         result = 'Characters unique'
#     else:
#         result = 'Characters not unique'
#     return result
        
# print (unique_characters(s))


s=input('Write a string: ')

def unique_characters(s):
       sorted_s=sorted(s)
       for index_letter in range(0, len(sorted_s) - 1):
           if sorted_s[index_letter] == sorted_s[index_letter+1]:
               return False
       return True
        
print (unique_characters(s))

#3. Write a function that calculates [Fibonacci series]. The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
#The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. A number of iterations should be taken from user input.
#def fibonacci(n):
    # your code here
#fibonacci(10)
#>>> 55

f1=int(input('1st value: '))
f2=int(input('2nd value: '))
# n = int(input('How uch numbers to show: '))
# def fibonacci(f1: int, f2: int, n: int) -> int:
#     print(f1, f2)
#     for i in range(2, n):
#         f1, f2 = f2, f1+f2
#         print(f2)
#     return f2

# fibonacci(f1, f2, n)

n = int(input('What numbers to show: '))

def fibonacci(f1: int, f2: int, n: int) -> int:
    i=0    
    while i<n-2:
        fib=f1+f2
        f1=f2
        f2=fib
        i=i+1
    return f2

result = fibonacci(f1,f2,n)
print (result)

#1st vercion
# while n > 2:
#     f1, f2 = f2, f1+f2
#     print(f2)
#     n -= 1

#2nd vercion
# print(f1,f2)
# for i in range(2,n):
#     f1, f2 = f2, f1+f2
#     print(f2)

# 4. Write a function that implements case swapping. It should return the same result as swapcase() method. 
#Your function should accept one str argument and convert all lower case values to upper case and vice versa. 
# def swapcase(input_string: str) -> str:
#     # do something
# print(swapcase('HelLo!')) 
# >>> 'hELlO!

input_string = input("Enter a text ")
end_string = input_string
for letter in input_string:
    if letter.isupper():
        end_string = letter.lower()
    if letter.islower():
        end_string = letter.upper()
    print(end_string,end="")

# 5. Write a function that calculates the performance of a deposit in a bank account. 
#The function called simple_interest takes three arguments: the initial amount, the annual interest rate (as a float), and the time in years. 
#The function should return the final amount after the simple interest has been applied. Use a for loop to accomplish this. Round the answer to the nearest hundredth.
# def simple_interest(initial_amount, interest_rate, years):
#     # Your code here
# print(simple_interest(10000, 0.1, 10))
    
    # initial_amount=int(input('Initial amount: '))
# rate=float(input('Annual interest rate, %: '))
# years=int(input('Time in years: '))

# def simple_interest (initial_amount, rate, years):
#     simple_interest_round=round((initial_amount*(1+rate/100*years))/100,0)*100
#     print(simple_interest_round)

# result_increased=simple_interest(initial_amount,rate,years)
# print(result_increased)

#simple_interest
initial_amount=int(input('Initial amount: '))
rate=float(input('Annual interest rate, %: '))
years=int(input('Time in years: '))

def simple_interest (initial_amount, rate, years):
    total_interest=0
    for year in range(1,years+1):
        interest_for_year = initial_amount*(rate/100)
        total_interest +=interest_for_year
        total_amount = initial_amount + total_interest
    return round(total_amount/100)*100

result_increased=simple_interest(initial_amount,rate,years)
print(result_increased)

#compound interest
initial_amount=int(input('Initial amount: '))
rate=float(input('Annual interest rate, %: '))
years=int(input('Time in years: '))

def compound_interest (initial_amount, rate, years):
    total_amount = initial_amount * (1+rate/100)**years
    return round(total_amount/100)*100

result_increased_2=compound_interest(initial_amount,rate,years)
print(result_increased_2)

# 6. (Optional) Write a function called password_strength that takes a string password as an argument and returns a password strength score based on the following criteria:
#     Lowercase letters: +2 points for each unique lowercase letter
#     Uppercase letters: +3 points for each unique uppercase letter
#     Digits: +4 points for each unique digit
#     Special characters: +5 points for each unique special character
# Use for loops to accomplish this. The function should return the total score for the given password.
# def password_strength(password):
#     # Your code here
# password_strength('abc123')
# >>> 24  #  6 for each symbol + 3 * 2 for each lowercase letter + 4 * 3 for each digit

#skipped for now

# 7. (Optional) Write two functions, encrypt and decrypt, that implement the [Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher) technique for encrypting and decrypting messages. The encrypt function should take a message and a shift value as arguments, while the decrypt function should take an encrypted message and the same shift value as arguments. Use for loops to accomplish this.
# def encrypt(message, shift):
#     # Your code here
# def decrypt(encrypted_message, shift):
#     # Your code here

#skipped for now