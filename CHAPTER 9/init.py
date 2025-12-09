class student:
    schoolname = "ABC High School"
    
    def __init__(self, name):
        print("Whenever a new object is created, this message will be printed.")
        self.name = name
        print(self)
        print(self.name)

stu1 = student("vijay") # intit method will be called

stu2 = student("Khumesh")