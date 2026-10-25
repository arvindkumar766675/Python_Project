# Project_1
correct_pin = "1234"
balance = 10000
transactions = []
attempts = 3
pin_correct = False

while attempts > 0:
    entered_pin = input("Enter PIN: ")
    if entered_pin == correct_pin:
        pin_correct = True
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")

if pin_correct:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Balance:", balance)
            
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance = balance + amount
                print("New balance:", int(balance))
                transactions.append(f"Deposit {int(amount)}")
            else:
                print("Invalid deposit amount.")
                
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficent balance")
            elif amount > 0:
                balance = balance - amount
                print("New balance:", int(balance))
                transactions.append(f"Withdraw {int(amount)}")
            else:
                print("Invalid withdrawal amount.")
                
        elif choice == "4":
            print("Thank you!")
            if len(transactions) > 0:
                print("\nTransaction History:")
                for t in transactions:
                    print(t)
            break
            
        else:
            print("Invalid choice, please try again.")

# Project_2
students = {
    "Aman": [85, 90, 78], 
    "Riya": [92, 88, 95], 
    "Zoya": [70, 65, 80]
}

while True:
    print("\n--- Student Menu ---")
    print("1. Add student")
    print("2. View all (Averages & Grades)")
    print("3. Show topper")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        
        if name in students:
            print("Student already exists.")
            continue
            
        marks = []
        while len(marks) < 3:
            m = float(input(f"Enter mark {len(marks) + 1} (0-100): "))
            if m < 0 or m > 100:
                print("Invalid mark, try again.")
            else:
                marks.append(m)
                
        students[name] = marks
        print("Student added successfully!")
        
    elif choice == "2":
        print("\nStudent Averages and Grades:")
        for name in students:
            lst = students[name]
            total = 0
            for mark in lst:
                total = total + mark
            avg = total / 3
            
            # Grade calculation
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
                
            print(name, round(avg, 2), grade)
            
    elif choice == "3":
        highest_avg = 0
        topper_name = ""
        
        for name in students:
            lst = students[name]
            total = 0
            for mark in lst:
                total = total + mark
            avg = total / 3
            
            if avg > highest_avg:
                highest_avg = avg
                topper_name = name
                
        print("Topper:", topper_name)
        
    elif choice == "4":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")