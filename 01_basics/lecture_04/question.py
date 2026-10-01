QN 1
Store following word meanings in a python dictionary:

table: "a piece of furniture", "list of facts & figures"
cat: "a small animal"

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture","list of facts & figures"]
}

print(dictionary)


QN 2
for students You are given a list of subjects Assume one classroom is required for 1 subject.
 How many classrooms are are needed by all students.

"python", "java", "C++", "python", "javascript",

"java", "python","java", "C++", "C"

subjects = {
    "python", "java", "C++", "python", "javascript",
 "java", "python","java", "C++", "C"
}
print(len(subjects))


QN 3
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. 
Use subject name as key & marks as value.

marks ={}

x = int(input("Enter marks of phy: "))
marks.update({"physics":x})

y = int(input("Enter marks of math: "))
marks.update({"mathematics":y})

z = int(input("Enter marks of chem: "))
marks.update({"chemistry":z})

print(marks)


QN 4
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)

values ={9, 9.0,3.4,4,4.0}
print(values)

values = {8,"8.0"}
print(values)

values = {
    ("float",6.0),
    ("int",5),

    ("string","zaid")
}
print(values)