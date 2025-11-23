# Write a program that:
# 1. takes user input as a sentence
# 2. prints the sentence in uppercase
# 3. prints the sentence in lowercase
# 4.replace all apaces with underscores
# 5. print new string

sentence= input("Enter a sentence:")

uppercase= sentence.upper()
print("U:"+uppercase)

lowercase= sentence.lower()
print("l:"+lowercase)

new_string= sentence.replace(" ","_")
print("new_string:"+new_string)
