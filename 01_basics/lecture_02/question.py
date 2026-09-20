#QN 1
#write a program to input users frist name and print its length.

name = input("enter your name:")
print("length of your name is",len(name))


# QN2
# WAP to find the occurrence of "$" in a string

str = "hi , iam  $ the $ symbol $12.22"
print(str.count("$"))


#QN 3
#write to check if a number enterd by the user is odd or even

num = int(input("enter number:"))

rem = num % 2

if(num% 2 == 0):
    print("Even")
else:
    print("Odd")


#QN 4
# write a program to find the greatest of 3 number  entered by the user

a = int(input("enter frist number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("frist number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third number is largest",c)



#QN 5
#write to check if a number is a multiple of 7 or not

x = int(input("enter number:"))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")