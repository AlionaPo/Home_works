#From None to Hero: Mastering Boolean and Strings

numbers='123456789'

#Make all these expressions true.
#b) 10 __ 5
print(10>5)
#c) 42 __ "42"
print(42==42)
#a) 3 __ 4
print(3!=4)

#1.Print the text in which there will be a quote with double quotes.
print('She said: "All is good"')
#2.Get a string from user input. Check if the string is a palindrome.
text=input()
print(text==text[::-1])

#3.The program receives the user's name and age from the input. 
name=input()
age=input()
#Then you need to display the name and age in one line in several ways: 

#- by listing all the parameters in the print function
print("Your name is "+name+" and your age is "+age+" years old")
#- by formatting a string using the format function
print("Your name is {0} and your age is {1} years old".format(name,age))
#- by formatting a string with f-string
intro =f"Your name is {name} and your age is {age} years old"
print(intro)

#Format string with proper built-in function

#All letters must be written in lowercase.
string_1="Animals  "
print(string_1.lower())

#All letters must be capitalized.
string_2="  Badger"
print(string_2.upper())

#Remove all spaces:
string_3 = "   HoneyPot   "
#a) from the beginning of the line
print(string_3.lstrip())
#b) from the end of the line
print(string_3.rstrip())
#c) on both sides of the line
print(string_3.strip())

#Check the value of the startwith('Be') function for each line.:
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"
print("Be" in string_1,"Be" in string_2,"Be" in string_3,"Be" in string_4)

#Convert these bear-like rows with methods from the previous exercise to have a positive result for each row.
formatted_string2 = 'Be'+string_2[2:]
formatted_string3 = string_3.replace(string_3[1],"Be",1)
formatted_string4 = 'Be'+string_4[2:]
print("Be" in formatted_string2, "Be" in formatted_string3, "Be" in formatted_string4)