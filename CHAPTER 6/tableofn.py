# write a program to print multplication table of any number

n = int(input("Enter any number:"))
print("Multiplication table of", n, "is:")
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i +=1

print("___________________ Table complete ________")