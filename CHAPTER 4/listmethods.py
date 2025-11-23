# Methods in list

#indexing
marks= [90,55,80,98,90,77]
print(marks)  
print("\n")

marks[1]= 88
print(marks)
print(marks[1])

# sclicing 
print(marks[1:3])  # it will print from index 1 to index 2

print(max(marks))  
print(min(marks))  

marks.append(99)
print(marks,"\n")

marks.insert(3,85)
print(marks,"\n")

marks.remove(88)
print(marks,"\n")

marks.pop(4)
print(marks,"\n")

marks.sort()
print(marks,"\n")

marks.reverse()
print(marks,"\n")
