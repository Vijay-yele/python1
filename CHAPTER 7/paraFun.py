


# functionn definition with parameters
def average(a=24,b=28): # a and b are default values if arguments not passed
    averavevalue= (a+b)/2
    print(averavevalue)
    
    


# Write a function show_age(name, age) that prints: "Saumya Singh is 21
# years old."

def show_age(name="vijay", age=20):
    print(f"{name} is {age} years old")
    



# 3. Write a function fav_food(food) that prints "Saumya loves <food>".

def fav_food(food= " Gulab jamun"):
    print(f"Saumya loves{food}")
    
# Create a function add_numbers(a,b) that prints both sum and difference

def add_numbers(a=10, b=35):
    sum = a+b
    difference= a-b
    print(f"sum is: {sum}")
    print(f"Difference is: {difference}")



# calling with Arguments
average(8,6)
average(56,23)
average(58,36)
average()


show_age("Saumy Singh",25)
show_age()


fav_food()

add_numbers(52,49)