# wriete a program to read a text from a given fie certificate.txt and find whether it  contains the word ive


file = open("certificate.txt", "r") # if file does not exist gives error 
dataofFile = file.read()

dataofFile = dataofFile.lower()

if "live" in dataofFile:
    print("Yes, the word 'live' is present in the file.")
else:
    print("No, the word 'live' is not present in the file.")