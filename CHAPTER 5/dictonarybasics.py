# dictonary basics

student = {
    "name":"Vijay",
    "city":"Gondia",
    "age":"20",
    "rollUnumber":33
    
}

print(type(student))
print(student)
print(student["name"])

student["city"] = "Nagpur"
print(student)

student["favSubject"]="Biology"
print(student)

student.pop("favSubject")
print(student)

print(student.keys())

print(student.values())

print(student.items())

