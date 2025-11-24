# Write a program that print the sum of first n natural numbers 

n = int(input("Enter a natural number: "))
sum = 0
i = 1
while (i <= n):
    sum += i
    i += 1
print("The sum of first", n, "natural numbers is:", sum)


# another way to do the same task
m = int(input("Enter a natural number: "))
sum1 = 0
while (m>=1):
        sum1 +=m
        m -=1
print("sum = ", sum1)
print("m=", m)