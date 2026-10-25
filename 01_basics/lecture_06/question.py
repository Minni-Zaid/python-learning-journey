QN 1
WRITE A FUNCTION TO PRINT THIE LENGTH OF A LIST (LIST IS THE PARAMETER)

cities=["bangalore","chennai","mumbai"]
skils=["linux","cloud","netowrking","python","bash"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(skils)


QN 2   
WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE (LIST IS THE PARAMETER)

cities=["bangalore","chennai","mumbai"]
skils=["linux","cloud","netowrking","python","bash"]

# print(cities[2],end=" ")
print(skils[3], end=" ")


def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(skils)


QN 3
WAF TO FIND THE FACTORIAL OF N.(N IS THE PARAMETER)

n=5

def cal_fact(n): 
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)  

cal_fact(10)


QN 4
WAF TO CONVERT USD TO INR

def converter(usd_val):
    inr_val = usd_val*95
    print(usd_val,"USD",inr_val,"INR")

converter(500)



      RECURSION FUNCTION

QN 1
WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)


QN 2
WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST
HINT : USE LIST AND INDEX AS PARAMETERS

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

veg = ["carrot","beans","cucumber","beetroot"]
print_list(veg)