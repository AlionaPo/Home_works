
#1 Write a program that gets two int variables and swaps their values. Do it in 3 different ways
a=int(input())
b=int(input())
#1
a2=a
a=b
b=a2
#2
a=a+b
b=a-b
a=a-b
#3
a, b = b, a
print(a)
print(b)

#2 Write a program that gets 2 numbers from the user. Print to the console their difference. Use the built-in Input function for that
c1=int(input())
c2=int(input())
print(c1-c2)

#3 Write a program that gets 2 numbers from the user. Print to the console maximum of these two variable. Use a built-in function for that
d1=int(input())
d2=int(input())
e=max(d1,d2)
print(e)

#Optional: Write a program that gets 3 digit number from the user and reverses it. You can use only numbers and their operators. Don`t use a string here!
h=int(input())
h1=h%10
h2=(h//10)%10
h3=h//100
h0=h1*100+h2*10+h3
print(h0)