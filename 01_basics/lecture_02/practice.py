name = input("enter your name:")
print("length of your name is",len(name))


str = "hi , iam the $ symbol $12.22"
print(str.count("$"))   



light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")

print("end of program")




num = 6
if(num>= 3):
    print("greater than 3 ")
if(num>=4):
    print("greater than 4")



age = 17

if(age>=18):
    print("can vote")
else:
    print("cannot vote")



marks = int(input("enter your marks:"))


if(marks>=90):
    print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>70 and marks<80):
    print("grade C")
elif(marks>60 and marks<70):
    print("grade D")
    
else:
    print("grade E")


age=89

 nesting
if(age>=18):
    if(age>70):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


num = int(input("enter number:"))

rem = num % 2

if(num% 2 == 0):
    print("Even")
else:
    print("Odd")



a = int(input("enter frist number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("frist number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third number is largest",c)




x = int(input("enter number:"))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")