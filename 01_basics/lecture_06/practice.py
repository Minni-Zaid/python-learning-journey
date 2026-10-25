def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum


calc_sum(10,20)


a = 10
b = 20

sum = a+b
print(sum)

more lines of code 

calc_sum(2,6)

a = 2
b = 6

sum = a+b
print(sum)

more no of lines of code

calc_sum(11,9)

a = 11
b = 9

sum = a+b
print(sum)

    OR


function definiaton
def calc_sum(a,b): #parameters
    return a + b

sum = calc_sum(5,90)  #function call: #Arguments
print(sum)

def print_hello():
print("hello")

print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()
print(output) #none

avarage of 3 numbers

def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

cal_avg(100,100,100)

print("cloud engineer","devops engineer")

print("cloudengineer",end=" ") #sep =" "
print("zaid") #end ="\n"


Default Parameters:
def cal_prod(a,b=5):
    print(a*b)
    return a*b

cal_prod(5)

        RECURSION function

def show(n):
    if(n==0):
        return n
    print(n)
    show(n-1)
    print("END")

show(3)   

def fact(n):
    if(n == 1 or n ==0):
        return 1
    return fact(n-1)* n

print(fact(4))
