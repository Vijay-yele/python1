#question 1 - create a dctonary named marks to store marks f 3 subjects. Add the subject one by one and print the final dictonary.

print("Question 1:-")

marks = {}
marks["Maths"] = 85
marks["Science"] = 92
marks["English"] = 86

print(marks)

# Question 2 :- you are given a list of programming languages:
# ["Python", "Java", "C++", "Java", "Python", "C"]
#Convert it into a set and print howmany unique languages Divya knows

print("Question 2:-")

programminglist= ["Python", "Java", "C++", "Java", "Python", "C"]

programmintset = set(programminglist)
print(type(programmintset))

print("Divya knows", len(programmintset), "unique programming languages.")

print("Divya knows these languages:", programmintset)


