# Print  how many lines are there in the file certificate.txt
import os

try:
    with open("certificate.txt", "r") as f:
        lines = f.readlines()
        numberoflines = len(lines)
        print("Number of lines in certificate.txt:", numberoflines)
except FileNotFoundError:
    print("The file certificate.txt does not exist.")   
    
# rename the file certificate.txt to mycertificate.txt

# os.rename("certificate.txt", "mycertificate.txt")

# for delete use remove method of os module