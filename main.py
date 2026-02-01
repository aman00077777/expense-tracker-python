# Expense Tracker Project

expenses = []
print("Welcome to the Expense Tracker!💸 | Kharcha kam kiya karo 💰!!!")

while True:
    print("\n✨=====MENU=====✨")
    print("1. Add Expense 📝")
    print("2. View Expenses 📋")
    print("3. View Total Kharcha 💰")
    print("4. Exit 🚪")

    choice = int(input("Choose an option (1-4): "))

    # Add Expense
    if choice == 1:
        date = input("Enter date (DD-MM-YYYY)🗓️: ")
        category = input("Enter category (e.g., Food, Travel)✌️: ")
        description = input("Enter description📝: ")
        amount = float(input("Kitna Kharcha Kiye ?🤨: "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)
        print("\nKharcha Jod diya gya! ✅")

    # View Expenses
    elif choice == 2:
        if not expenses:
            print("\nKoi Kharcha Nahi Hai! jao phele kharcha kro😌")
        else:
            print("\n=====📋Aapke Sabhi Kharchay=====")
            for i, eachKharcha in enumerate(expenses, start=1):
                print(f"{i}. Date: {eachKharcha['date']}, Category: {eachKharcha['category']}, Description: {eachKharcha['description']}, Amount: ₹{eachKharcha['amount']}")

    # View Total Expense
    elif choice == 3:
        total = sum(eachKharcha['amount'] for eachKharcha in expenses)
        print(f"\nAapka Total Kharcha Hai: ₹{total} 💸")

    # Exit
    elif choice == 4:
        print("\nDhanyawaad Aapne Humara System use kiya 🙏")
        break

    else:
        print("\nInvalid choice! Please select a valid option.❌")







