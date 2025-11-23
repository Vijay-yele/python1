# take num as input convert to folat and print boath converted and original
x = 5
y = 7
num = input("Enter a number: ")
print("Original input:", num)

num_converted= float(num)
print("Converted to float:", num_converted)

print("original",type(num))
print("converted",type(num_converted))

# comparison operator
print("\ncomparison operators")
print(5 > 3)  # greater than - true
print(5 < 3)  # less than -false
print(5 == 3) # equal to -false
print(5 != 3) # not equal to - true
print(5 >= 3) # greater than or equal to- true
print(5 <= 3) # less than or equal to - false

# logical operators
print("\nlogical operators")
print(x>y and x<y) # and - false
print(x>y or x<y) # or - true
print(not(x>y)) # not - true

