# with keyword

# file = open("report.txt", "r")
# data = file.read()

# file.close()

# with  open("data.txt", "r") as f:
#     data = f.read()
#     print("File data:", data)

with open("newText.txt", "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
#     line4= f.readline()
#     line5 = f.readline()
#     line6 = f.readline()
#     data = f.read()
    
#     print("Line 1:", line1)
#     print("Line 2:", line2)
#     print("Line 3:", line3)
#     print("Line 4:", line4)
#     print("Line 5:", line5)
#     print("Line 6:", line6)
#     print("file data:", data) # will give empty line
    
    
    
    readLinesMethod = f.readlines()
    print(readLinesMethod) # Will give output as  a list of lines in the file
    