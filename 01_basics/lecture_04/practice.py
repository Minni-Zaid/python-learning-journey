information = {
    "name" : "Minni zaid",
    "Age": 20,
    "Branch" : "CSE",
     78.90 : 90.4
}
print(type(information))
print(information)



information = {
    "name" : "zaiyan ",
    "Age": 20,
    "Branch" : "CSE",
     78.90 : 90.4
}

print(information["name"])
print(information["Age"])
print(information["Branch"])

information["name"] = "Minni"
information["surname"] = "zaid"

print(information)

null_dict ={}
null_dict["name"] = "Eloquence"
print(null_dict)


student = {
    "name" : "zzz",
    "Subject" :{"maths":90,
                "physics":89,
                "toc":80
    }
}
print(student["Subject"]["toc"])


Student = {
    "name" : "minizzzz",
    "Subject" :{"maths":90,
                "physics":89,
                "toc":80
    }
}

print(Student.keys())

print(Student.values())
print(list(Student.values()))

print(len(list(Student.keys())))
print(len(Student))  

print(Student.items())
print(list(Student.items()))

pairs = list(Student.items())
print(pairs[1])

print(Student["name"])
print(Student.get("name"))

print(Student["Subject"])
print(Student.get("Subject"))

new_dict = {"name":"alex","Age":20}
Student.update(new_dict)

print(Student)

SET IN PYTHON

collection = {1,1,2,3,3,3,4, "Hello","Zaid","Zaid"}
print(collection)

# print(type(collection))
print(len(collection))

collection ={}
print(type(collection))


collection = set()
print(type(collection))


collection = set()
collection.add(5)
collection.add(8)
collection.add(8)

collection.remove(6)
print(collection)


collection = set()
collection.add("minni")
collection.add("mohamed")
collection.add("zaid")

collection.add((1,2,3))
collection.add((3,4,6,))

collection.clear()
print(len(collection))


collection ={"hello","zaid","python","coding"}
print(collection.pop())
print(collection.pop())


set1 = {1,2,3,4,5}
set2 = {3,5,6,7,8}

print(set1.intersection(set2))
print(set1)
print(set2)