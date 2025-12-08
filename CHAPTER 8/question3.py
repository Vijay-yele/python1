# open a file in "x" mode to create a new file

file = open("data.txt", "x")  # if file already exists, it will give an error
file.write("This is a new file created in exclusive creation mode.\n")