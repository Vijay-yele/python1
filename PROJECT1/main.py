# Expense Tracker Project

expenseslist = [] # list of expense in form of dictonary
print("====Welcome to Expense Tracker====")

while True:
    print("======MENU======")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    
    choice= int(input("Please Enter Your Choice: "))
    # ADD EXPENSES
    if(choice==1):
        date= input("Enter the Date of Expenses:")
        category= input("Enter Type of Expense(Food, Travel, Mackup, Books, Games):")
        description= input("Enter More Detials:")
        amount= float(input("Enter the Amount:"))
        
        expense ={
            "date": date,
            "category":category,
            "description": description,
            "amount": amount
        }
    
        expenseslist.append(expense)
        print("\n********Expenses Added Succesfully**********\n")
    
    # 2. VIEW ALL EXPENSES
    
    elif(choice==2):
        if(len(expenseslist)==0):
            print("NO Expenses Added Till Now. ")
        else:
            print("======THis is Your All Expenses======")
            count = 1
            for everyexpense in expenseslist:
                print("Expense Number",count,"->","On date",everyexpense["date"],",Of type:",everyexpense["category"],",description:",everyexpense["description"],",amount",everyexpense["amount"])
                count +=1
    
    # 3. VIEW TOTAL SPENDING
    elif(choice==3):
        total=0
        for everyexpense in expenseslist:
            total = total + everyexpense["amount"]
        
        print("\nTOTAL EXPENSE=",total)
    
    # 4.EXIT 
    elif(choice==4):
        print("=========THANK YOU FOR USINNG EXPENSE TRACKER======")
        break
    else:
        print("INVALID COICE. TRY AGAIN")
        

