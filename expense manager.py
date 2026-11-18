# persional finance app
expenselist =[]
print("welcome personal finance app: manage your expenses")

while True:
    print("==**==MENU==**==")
    print("1. add expense")
    print("2. view all expenses")
    print("3. view total expenses")
    print("4. exit app")

    choice = input("please enter your choice:")

#ADD expense                   
    if (choice == "1"):
     date = input("in which date did you spend the money?:")
     category = input("what type of category your expense is?:")
     description =input("can you give me more details aboudt your expenses?:")
     amount = float(input("enter your spended amount:"))

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
   
    expenselist.append(expense)
    print(" \n your expense has been successfully added sir !!")

#2 view all expenses
    if(choice == "2"):
         if len(expenselist) == 0:
            print("you has not added any expaenses in this !!")
         else:
           print("this is your total expexse is here sir !")
           count = 1
           for eachexpense in expenselist:
               print(f"expensenumber {count} >> {eachexpense["date"]},{eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]}")
               

#3 VIEW TOTAL SPENFIND
    if (choice == "3"):
           total = 0 
           for eachexpense in expenselist:
               total = total + eachexpense["amount"]

           print("\n your total expense is =", total)

#4 exit the app
    elif (choice =="4"):
         print("Thank You for using our app sir !!")
         break
    else:
         print("something went wrong please try again sir/ madam")
