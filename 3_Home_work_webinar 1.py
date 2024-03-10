#1 Area of a  Triangle Given its Vertices
#Write a function triangle_area that calculates the area of a triangle given its vertices (x1, y1), (x2, y2), and (x3, y3). 
#The formula for the area of a triangle given its vertices is:
#Area = 1/2 |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
x1, y1=int(input('x1= ')), int(input('y1= '))
x2, y2=int(input('x2= ')), int(input('y2= '))
x3, y3=int(input('x3= ')), int(input('y3= '))
print(1/2*abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))

#2 Count a number of words in the sentence
#sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."count_words(sentence) == 12
import re
sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."
words = re.findall(r'\b\w+\b',sentence)
words_count = len(words)
print(words_count==12)

# version 2
words_ver_2 = sentence.split(' ')
counter = 0
for word in words_ver_2:
    new_word = ''
    for symbol in word:
        if symbol.isalpha():
            new_word += symbol
    if new_word:
        counter += 1
print(counter==12)

#vercion 3
def count_words(sentence):
    words_ver_2 = sentence.split(' ')
    # print(words_ver_2)
    counter = 0
    for word in words_ver_2:
        new_word = ''
        for symbol in word:
            if symbol.isalpha():
                new_word += symbol
        if new_word:
            counter += 1
    return counter

print(count_words(sentence) == 12)

#version 4
count_words = len([word for word in sentence.split(" ") if any(symbol.isalpha() for symbol in word)])

# words_v2 = sentence.split()
# words_count_v2 = sum(1 for x in words_v2 if x.isalpha())
# print(words_count_v2==12)

#3 snake_case to CamelCase convertor
#Write a code that convert string from snake case format to camel case. start_string = "snake_case_text" end_string = "SnakeCaseText"
start_string = "snake_case_text"
camel_case_text=start_string.title()
end_string= camel_case_text.replace('_','')
print(end_string)

#3 - 2nd idea
def snake_to_camel (snake_string):
    words = start_string.splitt('_')
    camel_string = ''
    for word in words:
        camel_string += word.capitalize()
    return (camel_string)

end_string = snake_to_camel(start_string)
print (end_string)

#4 FizzBuzz
#Write a function fizz_buzz that prints the numbers from 1 to a given number n. 
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
#For numbers which are multiples of both three and five print “FizzBuzz”.
n=int(input('n= '))
for x in range(1,n):
    if x%3==0 and x%5==0:
        print("FizzBuss")
    elif x%3==0:
        print ("Fizz")
    elif x%5==0:
        print("Buss")
    else: 
        print(x)

#5 CamelCase to snake_case convertor
#start_string = "SnakeCaseText" end_string = "snake_case_text"
import re
start_string = "SnakeCaseText"
snake_case_text=re.sub(r'(?<!^)(?=[A-Z])','_',start_string).lower()
print(snake_case_text)

#version 2
start_string = "SnakeCaseText"

end_string = start_string[0].lower()
for letter in start_string[1:]:
    if letter.isupper():
        end_string += '_' + letter.lower()
    else:
        end_string += letter
print(end_string)

#Anagrams
#Write a function called anagrams that takes in two strings s1 and s2 and returns a Boolean value indicating whether or not s1 and s2 are anagrams. 
s1=input('s1= ')
s2=input('s2= ')
s1, s2 = list(s1), list(s2)
s1.sort()
s2.sort()
print(s1==s2)