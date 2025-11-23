# write a python program that takes a number as input and prints:
# "Positive" if the number is greater than zero,
# "Negative" if the number is less than zero,
# and "Zero" if the number is equal to zero.

num = float(input(" Enter any random number:"))


if(num>0):
    print("positive")
elif(num==0):
    print("zero")
else:
    print("negative")