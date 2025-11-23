# Write a program that takes your favoirite fruit as input and prints:  the  middle three characters, tha last 2 characters

fruit = input(" Enter your favoirite fruit: ") # mango
length = len(fruit)
mid = length // 2
print(fruit[mid-1:mid+2]) # middle three character
print(fruit[-2:]) # last two character