#Dict-set Diaries: A Tale of Two Data Types

#1. Write a game where the user should guess the capital of the country that you have in your dictionary.

capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels',  'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens',
}

# You should show the user a random country from the list and ask him to guess the capital. 
# If the user inputs the right capital, print "You are right!", add a point and ask him to guess another country. 
# If not, you should ask again. The user should be able to quit the game by typing "exit".

# You should print the current score after each round. Also, you should print the final score before the user quit the game.

# Optional:

# 1. Give the user a hint if he guesses wrong. The hint should look like the first letter of the capital. 
# If the user makes another mistake, you should print one more letter from the capital.

# 2. If a user makes a mistake you should decrement his life. The initial amount of lives is 3. 
# The game will end when the user has no lives left. You should print the final score after the user has no lives left.

import random

point=0
get_capital = "" #for str better to use "" than 0, as 0 servs for Int
while get_capital.lower() != "exit": #assuming the user can enter lower cases
    get_country = random.choice(list(capitals.keys()))
    print(get_country)
    get_capital  = input("Write a capital for chosen country: ")
#     point=0
    if get_capital == capitals[get_country]:
        print ("You are right!")
        point += 1
        print ("Now points are:", point)
        continue
    elif get_capital.lower() == "Exit":
        print (f"You finished with {point} points:")
    else:
        get_capital != capitals[get_country] #not mandatory
        print("try again")
        get_capital  = input("Write a capital for chosen country: ")
        if get_capital == capitals[get_country]:
            print ("You are right!")
            point += 1
            print ("Now points are:", point)
# if get_capital == "Exit":
#print (f"You finished with {point} points:")


#version 2 
# while True:
#     get_country = random.choice(list(capitals.keys()))
#     print(get_country)
#     get_capital = input("Write a capital for choosen country: ")
#     help_answer = ''
#     while get_capital != capitals[get_country] and get_capital.lower() != 'exit':
#         print('Wrong answer, try again')
#         lives -= 1
#         if lives == 0:
#             break
#         get_capital = input("Write a capital for choosen country: ")
#         if get_capital.lower() == 'exit':
#             break
#         help_answer = capitals[get_country][:len(help_answer) + 1]
#         print(f'Tips: {help_answer}')
#     if lives == 0 or get_capital.lower() == 'exit':
#         print('Game finished', point)
#         break
#     point = correct_answer(point)

#version 3
# get_country = random.choice(list(capitals.keys()))
# help_answer = ''

# while True:
#     print(get_country)
#     get_capital = input("Write a capital for choosen country: ")
#     if get_capital == capitals[get_country]:
#         get_country = random.choice(list(capitals.keys()))
#         point += 1
#         help_answer = ''
#     elif get_capital.lower() == 'exit':
#         break
#     else:
#         lives -= 1
#         if lives == 0:
#             break
#         help_answer = capitals[get_country][:len(help_answer) + 1]
#         print(f'Tips: {help_answer}')
# print('Game finished', point)



#2 Optional Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol Value
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written from largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# can be placed before D (500) and M (1000) to make 400 and 900.

# Given a Roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# def roman_to_int(s: str) -> int:
#       # write your code here

# def test_roman_to_int():
#      result1 = roman_to_int("III")
#      assert result1 == 3
#      result1 = roman_to_int("LVIII")
#      assert result1 == 58
#      result1 = roman_to_int("MCMXCIV")
#      assert result1 == 1994


#vercion 1:
# ROMANS = {
#     "M": 1000,
#     "D": 500,
#     "C": 100,
#     "L": 50,
#     "X": 10,
#     "V": 5,
#     "I": 1
# }

# SUB_ROMANS = {
#     "CD": 400,
#     "CM": 900,
#     "IV": 4,
#     "XL": 40,
#     "IX": 9,
#     "XC": 90
# }

# def roman_to_int(s: str) -> int:
#     result = 0
#     while len(s) > 0:
#         if s[:2] in SUB_ROMANS.keys():
#             result += SUB_ROMANS[s[:2]]
#             s = s[2:]
#         else:
#             result += ROMANS[s[:1]]
#             s = s[1:]
#         print(s, result)

#     print(result)            


# 3. Optional Try to create a function that will do reverse operation - from integer to Roman

#     def int_to_roman(s: str) -> int:
#         # write your code here

#     def test_int_to_roman():
#         result1 = int_to_roman(3)
#         assert result1 == "III"

#         result1 = int_to_roman(58)
#         assert result1 == "LVIII"

#         result1 = int_to_roman(1994)
#         assert result1 == "MCMXCIV"



# 4. Given a list of integers of size n, return the majority element.
# The majority element is the element that appears more than any other element. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#     def majority_element(nums: list) -> int:
#         # write your code here
    
input_nums = (input('Enter figures with comma, w/o space and gaps: ').replace('[', '').replace(']', '').split(','))
input_nums = [int(x) for x in sorted(input_nums)]

def majority_element(input_nums: list) -> int:
    max_count=0
    max_symbol=''
    start_count=0
    start_symbol=''
    for i in input_nums:
        if i==start_symbol:
            start_count+=1
        else:
                start_symbol=i
                start_count=1
        if start_count > max_count:
                max_count = start_count 
                max_symbol=start_symbol
    return max_symbol

result = majority_element (input_nums)
print (result)


def test_majority_element():
     result1 = majority_element([3, 2, 3])
     assert result1 == 3

     result1 = majority_element([])
     assert result1 == 2


#version2
# input_nums = (input('Enter figures with comma and a space as a separator: ').
#               replace('[', '').
#               replace(']', '').
#               split(','))
# input_nums = [int(x) for x in input_nums]

# def test_majority_element():
#     result1 = majority_element([3, 2, 3])
#     assert result1 == 3

#     result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
#     assert result1 == 2

# def majority_element(input_nums: list) -> int:
#     max_count = 1
#     max_number = input_nums[0]
#     for i in set(input_nums):
#         if max_count < input_nums.count(i):
#             max_number = i
#     return max_number

# result = majority_element(input_nums)
# print(result)


# 5. Find missing subjects
# You are a teacher at a school, and you have just finished grading a set of exams for your students. 
# Each student's exam is represented as a tuple containing their name, their score, and the subject of the exam. 
# You want to identify which subjects were not passed by all students so that you can give extra attention 
# to those subjects in your future lessons. Passing is defined as a score of 60 or higher. 
# Your task is to write a Python program that reads in a list of student exams, 
# identifies the subjects that were not passed by all students, and outputs a set of those subjects.

# def get_subjects_not_passed_by_all_students(student_exams):
#     pass

exams = [
    ("Alice", 55, "Math"),
    ("Bob", 40, "Math"),
    ("Charlie", 30, "Math"),
    ("Alice", 50, "Science"),
    ("Bob", 45, "Science"),
    ("Charlie", 40, "Science"),
    ("Alice", 95, "History"),
    ("Bob", 85, "History"),
    ("Charlie", 90, "History"),
]

def get_subjects_not_passed_by_all_students(exams):
    values = [x[2] for x in exams if x[1] > 60]
    all_exams = [x[2] for x in exams]
    not_passed = set(all_exams)-set(values)
    return not_passed
result_subjects = get_subjects_not_passed_by_all_students(exams)
print (result_subjects)

def test_get_subjects_not_passed_by_all_students():
     assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}


#version 2 & 3
#   def get_subjects_not_passed_by_all_students(exams):
#     exam_grouped = {}
#     for item in exams:
#         if not exam_grouped.get(item[2]):
#             exam_grouped[item[2]] = [item[1]]
#         else:
#             exam_grouped[item[2]].append(item[1])
#     res = []
#     for exam_name, exam_values in exam_grouped.items():
#         if max(exam_values) < 60:
#             res.append(exam_name)
#     return set(res)

# def get_subjects_not_passed_by_all_students(exams):
#     values = [x[2] for x in exams if x[1] < 60]
#     all_exams = [x[2] for x in exams]
#     res = []
#     for i in set(values):
#         if values.count(i) == all_exams.count(i):
#             res.append(i)
#     return set(res)      
     
#vercion 4
# def get_subjects_not_passed_by_all_students(exams):
#     return set([x[2] for x in exams])-set([x[2] for x in exams if x[1] > 60])
