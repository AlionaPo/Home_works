#Loop de Loop: The Endless Homework Chronicles

#1. Make all these expressions True by adding parentheses:    
False == (not True)
(True and False) == (True and False)
not (True and "A" == "B")
print(bool(not True) and ("A" == "B"))

#2. Make a solution for Wheat and chessboard problem. Represent a solution in tons. Assume that one grain of wheat weights 0.065 gram
Weight = int((2**64-1)*0.065/1000000)
print(Weight)

#3. Get a positive number from user input. Find all factors of this number.
a=int(input('Enter a value: '))
print(abs(a))
# for numbers_list in range(1,abs(a)+1):
#     print(numbers_list)
factors= []
for numbers in range(1,abs(a)+1):
    if (abs(a) % numbers)==0:
        factors.append(numbers)
print(factors)

# 4. Write a Python program to check whether a triangle is equilateral, isosceles or scalene. Get all three sides from user input.
#     Note :
# An equilateral triangle is a triangle in which all three sides are equal. A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
a=int(input('Enter a value for A side: '))
b=int(input('Enter a value for B side: '))
c=int(input('Enter a value for C side: '))
if a==b==c:
    print('equilateral triangle')
elif a!=b!=c:
    print('scalene triangle')
else:
    print('isosceles triangle')

# 5. Read the string and find its longest consecutive symbol.
#     Example
# Input: 'aaaabchjjjjjswwwwwwwxyzaaaaaa'
# Output: `Longest consecutive symbol: w`
string=input('Enter a string: ')

max_lenth=0
max_symbol=''
start_lenth=0
start_symbol=''
for i in string:
    if i==start_symbol:
          start_lenth+=1
    else:
            start_symbol=i
            start_lenth=1
    if start_lenth>max_lenth:
            max_lenth=start_lenth 
            max_symbol=start_symbol
print(max_symbol)

#vercion 2
string=input('Enter a string: ')
def longest_part(string):
    max_lenth=0
    max_symbol=''
    start_lenth=0
    start_symbol=''
    for i in string:
      if i==start_symbol:
         start_lenth+=1
      else:
         start_symbol=i
         start_lenth=1
      if start_lenth>max_lenth:
         max_lenth=start_lenth 
         max_symbol=start_symbol
    return max_symbol

print(longest_part(string))