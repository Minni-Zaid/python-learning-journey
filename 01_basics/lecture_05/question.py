# QNO 1
# print numbers from 1 to 100 using while loop

i = 1
while i <=100:
    print(i)
    i +=1

# QNO 2
# print numbers from 100 to 1 

i = 100
while i >=1:
    print(i)
    i -=1

#  QNO 3
#  print the multiplications table of a number n

n= int(input("Enter  number "))
i=1
while i<=10:
    print(n*i)
    i+=1


# Qno 4
# print the element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <len(nums):
    print(nums[idx])
    idx +=1

# traverse

tools =["Excel","Word","Powerpoint","Outlook"]
idx =0
while idx < len(tools):
    print(tools[idx])
    idx +=1


# qno 5
# Search for a number x in this tuple using loop [1,4,9,16,25,36,49,64,81,100]


nums = (1,4,9,16,25,36,49,64,81,100)
x = 64

i =0 #initialization

while i < len(nums):
   if (nums[i] == x):
     print("FOUND at idx",i)

   else:
       print("finding...")
   i +=1



# using for loop

# Qno 1
# print the element of the following lsit using a loop 
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)

# Qno 2
# search for a number x in this tuple using loop [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0
for el in nums:
    if (el == x):
        print(" number found at idx", idx)
        idx += 1

# USING FOR LOOP AND RANGE()

# QNO 1
# PRINT NUMBER FORM 1 TO 100

for i in range(1,101):
    print(i)

# QNO 2
# PRINT NUMBER FORM 100 TO 1

for i in range(100,0,-1):
    print(i)

# QNO 3
# PRINT THE MULTIPLICATION TABLE OF A NUMBER N

n = int(input("Enter a number: "))

for i in range(1,11):
    print(n*i)


# PASS STATEMENT
# QNO 1
# WAP TO FIND THE SUM OF FIRST N NUMNERS (USING WHILE LOOP)

n = 7
sum = 0
i=1
while i<=n: 
 for i in range(1,n+1): 
    sum +=i
    i+=1
print("total sum =",sum)

# QNO2
# WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS (USING FOR LOOP)


n = 3
fact = 1
i = 1

while i <= n:
 fact *= i
 i += 1

print("Factorial =", fact)

# same but in for loop

n=5
fact =1

for i in range(1,n+1):
 fact *=i
 print("factorial =",fact)