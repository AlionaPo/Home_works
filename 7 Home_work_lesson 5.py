#Try, Try Again: The Exceptional Tale of Tuples and Scope

# 1. Write a program that asks the user to enter an integer and convert it to an int. 
#v The program should have 2 functions. The first function should ask the user to input information and return inputted value. 
#v The second function receives the inputted value and converts it to int. 
#v If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. 
# if the user inputs an integer, the program should print this number and quit w/o any error.

def first_function():
    input_integer = input("Please enter an integer: ")
    return input_integer

def second_function(input_integer):
    while True:
        try:
            int_input = int(input_integer)
            return int_input
        except ValueError:
            print(f"{input_integer} is not an integer! Please try again.")
            input_integer = first_function()

number = first_function()
result = second_function(number)
print(result)
          

# 2. Write a program that asks the user to input a string and an integer n. The Program should have 2 functions. 
#The first function should ask the user to enter a string and an integer. 
#The second function should receive the inputted value and print the character at the index n. 
#If the user enters the wrong value, this function should catch an error and provide a proper error message with an explanation. 
#After the error is handled, the program should ask the user to enter a string and an integer again. 
#If the user inputs a string and an integer, the program should print the character at the index n and quit w/o any error.

def first_function():
    is_string_incorrect = True
    while is_string_incorrect:
        try:
            input_string = input("Enter a string: ")
            input_string[0]
            if not input_string.isalpha():
                print('Please enter only alphanumeric')
                continue
            is_string_incorrect = False
        except IndexError:
            print('String is empty')

    is_integer_incorrect = True
    while is_integer_incorrect:
        try:
            input_integer = int(input("Enter an integer: "))
            if len(input_string) <= input_integer:
                print(f'Please enter an integer that less than len of input string: {len(input_string)}')
                continue
            is_integer_incorrect = False
        except ValueError:
            print('Please enter an correct integer')

    return input_string, input_integer

def second_function(input_string, input_integer):
    return input_string[input_integer] 

input_string, input_integer = first_function()
print(second_function(input_string, input_integer))

# 3. Transaction
# a) Define a global variable called balance and set it to 1000. 
#    Write a function called transaction that takes an argument amount and argument _type that can be either deposit or withdrawal.              
# b) Inside the function create two inner functions called deposit and withdrawal that take an argument amount.              
# c) Inside the deposit function, add the amount to the balance variable and print the new balance.              
# d) Inside the withdrawal function, subtract the amount from the balance variable and print the new balance.              
# e) Inside the transaction function, check if the _type argument is deposit or withdrawal and call the appropriate function.

balance = 1000

def transaction(amount, _type):
    def deposit(amount):
        global balance
        
        balance += amount
        print(balance)

    def withdraw(amount):
        global balance

        balance -= amount
        print(balance)

    if _type not in ('deposit', 'withdraw'):
        raise Exception('Invalid transaction type')
    if amount <= 0:
        raise Exception('Amount is negative')

    # if _type != 'withdraw' or _type != 'deposit':
    #     raise Exception('Invalid transaction type')

    if _type == 'withdraw':
        withdraw(amount)
    else:
        deposit(amount)

transaction(100, 'withdraw')
transaction(200, 'deposit')


# 4. Write a function that simulates a dice roll and returns the result from 1 to 6. Use random module

import random

def dice_roll():
    return random.randint(1,6)

# 5. Use the function from the previous task to simulate 1000 dice rolls and print the result. Calculate the number of times each number was rolled.

results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,}
for i in range(1000):
    dice_results = dice_roll()
    results[dice_results] +=1
    print(dice_results)

for number, count in results.items():
    print(number, count)


# 6. Simulate an election for two candidates. 
# The program should take the number of regions and the rating for 1st candidate in each region (in percentage). 
# The program should run elections in every region. In every region, the program should ask 10 000 voters. 
# Use the random module to simulate a voice from a person. The candidate counts as a winner if he gains more than 50% of all votes. 
# The program should print the result of the election for each region and the winner
# Example:
# Enter the number of regions: 2
# Enter a rating for 1st candidate in 1 region: 34
# Enter a rating for 1st candidate in 2nd region: 56
# Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate
# Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate
# Result: 2nd candidate won with 10900 votes and 54.5% of all votes
# In your solution, you should use the input function to get the value from the user. 
# After that, use a random function to generate votes for your candidate. 
# After that calculate these votes and print the result. In your solution, you should implement these functions:

# *def* receive_input():
# pass
# *def* simulate_region_election():
# pass
# *def* simulate_election():
# pass
# *def* calculate_result():
# pass
# *def* announce_result():
# pass
# input_data = receive_input()
# election_result = simulate_election(input_data)
# result = calculate_result(election_result)
# announce_result(result)

import random

def receive_input():
    regions = int(input("regions amount: "))
    results = {}
    for r in range(regions):
        candidat_rating = float(input(f"Enter a rating for region {r+1}: "))
        results[r+1] = candidat_rating
    return results

results=receive_input()
print("ratings are:", results)

def simulate_election(results):
    election_results = {}
    for region, rating in results.items():
        first_candidate = 0
        second_candidate = 0
        for i in range(10000): 
            if random.random() < rating/100: 
                first_candidate += 1 
            else: 
                second_candidate += 1
        election_results[region] = {'Candidate 1': first_candidate, 'Candidate 2': second_candidate}
    return election_results

election_results = simulate_election(results)

for region, votes in election_results.items():
    print(f"Region {region} votes: {votes}")

total_votes_1 = 0
total_votes_2 = 0
for region, votes in election_results.items():
    total_votes_1 += votes['Candidate 1']
    total_votes_2 += votes['Candidate 2']

if total_votes_1 > 10000*len(results)*0.5:
    print ("Candidate_1 - won")
else:
    print ("Candidate_2 - won")