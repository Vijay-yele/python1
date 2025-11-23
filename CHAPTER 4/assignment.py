# assignment 1 - ask user to 3 movies name and store inn list

print("assignment 1:-")
movie1= input("Enter movie 1 name: ")
movie2= input("Enter movie 2 name: ") 
movie3= input("Enter movie 3 name: ")

movies=[movie1, movie2, movie3]
print(movies)
print(" ")

# assignment 2 - create tuple of marks and print highest and lowest marks
print("assignment 2:-")

markstup=(87,64,33,95,76)

print("maximum marks:",max(markstup))
print("minimum marks:",min(markstup))
print(" ")


# assignment 3 - write program to print gread based on marks
print("assignment 3:-")


marks= 73

if(marks>90):
    print("Gread A")
elif(marks>80 & marks< 90):
    print("Gread B")
elif(marks>70 & marks< 80):
    print("Gread C")
else:
    print("Gread D")
