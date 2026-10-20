import csv
import os
filename = "6.Read files/expenses.csv"
if not os.path.exists (filename):
    with open(filename , "w" , newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Date" , "Category" , "amount"])

while True:
    print("\n---EXPENSE TRACKER---")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        Date = input("Enter date(DD-MM-YYYY)")
        Category = input("Enter category:")
        amount = float(input("Enter amount:"))

        with open( filename, "a" , newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([Date, Category, amount])
        print("Expense saved succesfully!")

    elif choice == "2":
        with open(filename , "r" , newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice == "3":
        total = 0

        with open(filename , "r" , newline = "") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total += float(row["amount"])
        print("Total spending: Rs" , total)

    elif choice == "4":
        print("Thank You for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Please try again")
