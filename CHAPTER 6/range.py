# range(start, stop, step)

#Q 8 - write a program to print even numbers betwween 1 to 20 using for and range()
print("Even numbers between 1 to 20 are:")

for item in range(2,21,2):
    print(item)
    # 2,4,6,8,10,12,14,16,18,20
    
print("*******************************")

# break
for item in range(1,21,1):
    if item==10:
        break
    print(item)
    # 1,2,3,4,5,6,7,8,9
print("*******************************")

# continue
# Write a program that prints numbers 1 to 10, but skips the number 7 using the continue statement.

for item in range(1,11,1):
    if item == 7:
        continue
    print(item)
    # 1,2,3,4,5,6,8,9,10
    
print("*******************************")

# pass
for item in range(2,21,2):
    pass
    # this loop does nothing
print("********************************")

for i in range(5):
    print(i)
