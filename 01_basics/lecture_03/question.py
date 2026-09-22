QN1

write a program to ask the user to enter names
 of their 3 favorite movies and sotre them in a list

movies =[]
mov1 = input("enter 1st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
 
another type

movies =[]
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))

print(movies)



QN 2
write  a program to check if a list conatain 
a palindrome of element (hint:use copy()method)
        "racecar"  [1,2,3,2,1]

list1 = ["m","a","a","m"]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")



QN 3
write a program to count the number of students with the "A" 
grade in the following tuple

grade =("B","C","D","A","B","A")
print(grade.count("A"))


QN 4
store the above values in a list and sort them from "A" to "D"

grade =["B","C","D","A","B","A"]
grade.sort()
print(grade)