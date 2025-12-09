# Create class Student that takes 3 marks and has a method average

class Student:
    
    def __init__(self,name, list_of_marks=[]):
        self.name= name
        self.marks= list_of_marks
        
    def average(self):
        sum = 0
        for each in self.marks:
            sum = sum + each
        average = sum / len(self.marks)
        print("Average marks of", self.name, "is:", average)
        print()


Student1= Student("vijay",[98,91,90])
Student1.average()