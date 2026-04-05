# ##################### Step 1:FUNCTIONS AND LOGIC #############################
# from calendar import month
# from datetime import date, datetime
# import os
# import csv

# # loading data 
# def load_expenses():
#     expenses = []
    
#     if not os.path.exists("expenses.csv"):
#         return expenses
#     with open("expenses.csv",mode="r",newline="") as file:
#         reader =csv.DictReader(file)
#         for row in reader:
#             expenses.append({
#                 "amount": float(row["amount"]),
#                 "category": row["category"],
#                 "date": row["date"]
#             })
#     return expenses

# # save expense
# def save_expenses(expenses):
#     with open("expenses.csv",mode="w",newline="") as file:
#         fieldnames = ["amount","category","date"]
        
#         writer = csv.DictWriter(file,fieldnames=fieldnames)
#         writer.writeheader()
#         for expense in expenses:
#             writer.writerow(expense)
        
    
    
# ###### 1.ADD EXPESENSE: #######

# def add_expense(expenses, budgets):
#     try:
#         amount = float(input("Enter Amount: "))
#         if amount <= 0:
#             print("Amount must be greater than zero.")
#             return
#     except ValueError:
#         print("Invalid amount! Please enter a number.")
#         return
    
#     category = input("Enter Category: ")
#     date_input = input("Enter Date (YYYY-MM-DD): ").strip()

#     try:
#         datetime.strptime(date_input, "%Y-%m-%d")
#         date = date_input
#     except ValueError:
#         print("Invalid date format.")
#         return
    
#     if category.strip() == "" or date.strip() == "":
#         print("Category and date cannot be empty.")
#         return

#     expense = {
#         "amount": amount,
#         "category": category,
#         "date": date
#     }

#     expenses.append(expense)
#     save_expenses(expenses)
#     print("Expense added successfully.")

#     month = date[:7]

#     if month in budgets:
#         total = 0
#         for exp in expenses:
#             if exp["date"][:7] == month:
#                 total += exp["amount"]
#         percent = (total / budgets[month]) * 100
#         print(f"Budget used: {percent:.2f}%")

#         if total > budgets[month]:
#             over = total - budgets[month]
#             print(f"⚠ Warning: Budget exceeded for {month}")
#             print(f"Budget: {budgets[month]:.2f}")
#             print(f"Spent: {total:.2f}")
#             print(f"Over by: {over:.2f}")
            
# ###### 2.VIEW ALL EXPENSES: ######

# def view_expenses(expenses):
#         if len(expenses) == 0:
#             print("No expenses recorded yet.")    
#         else:
#             print("\n All Expenses: ")

#             for index,expense in enumerate(expenses,start=1):
#                 print(
#                     index,
#                     "Amount:", expense["amount"],
#                     "Category:", expense["category"],
#                     "Date:", expense["date"]
#                 )
                
# ###### 3.CALCULATE TOTAL EXPENSES: #########

# def total_expense(expenses):
#         total = 0
#         for expense in expenses:
#             total += expense["amount"]

#         print("Total Expense:",total)
       
# ###### 4.Delete Expenses: #########

# def delete_expenses(expenses):
#     if len(expenses) == 0:
#         print("No expenses to delete")
#         return
#     view_expenses(expenses)
    
#     try:
#         choice = int(input("Enter expense number to delete: "))
        
#     except ValueError:
#         print("Please enter a valid number.")
#         return

#     index = choice - 1

#     if index < 0 or index >=len(expenses):
#         print("Invalid expense number.")
#         return
    
#     deleted = expenses.pop(index)
#     save_expenses(expenses)  
    
#     print("Deleted Expenese",deleted)

# ###### 5.FILTER_BY_CATEGORY: #########

# def filter_by_category(expenses):
#     if len(expenses) == 0:
#         print("No expenses recoreded yet.")
#         return
#     category_input = input("Enter category to filter: ").strip().lower()

#     found =False
#     print("\nFiltered Expenses: ")

#     for expense in expenses:
#         if expense["category"].lower() == category_input:
#             print(
#                 "Amount:",expense["amount"],
#                 "Category:",expense["category"],
#                 "Date:",expense["date"],
#             )
#             found = True
#     if not found:
#         print("No expense found for this category.")  
        
# ###### 6.FILTER_BY_DATE: #########

# def filter_by_date(expenses):
#     if len(expenses) == 0:
#         print("No expense recorded yet.")
#         return
#     date_input =input("Enter date to filter (YYYY-MM-DD): ").strip()
    
#     found = False
#     print("Filtered Expenses: ")
    
#     for expense in expenses:
#         if expense["date"] == date_input:
#             print(
#                 "Amount:",expense["amount"],
#                 "Category:",expense["category"],
#                 "Date:",expense["date"],
#             )
#             found = True
#     if not found:
#         print("No expense found for this date")
 
# ###### 7.FILTER_BY_AMOUNT_RANGE: #########

# def filter_by_amount_range(expenses):
#     if len(expenses) == 0:
#         print("No expense recorded yet.")
#         return
    
#     try:
#         min_amount =float(input("Enter minimum amount: "))
#         max_amount =float(input("Enter maximum amount: "))
#     except ValueError:
#         print("Please enter valid numbers.")
#         return
    
#     if min_amount > max_amount:
#         print("Minimum amount cannot be greater than maximum amount.")
#         return
    
#     found = False
#     print("\nFiltered Expenses: ")
    
#     for expense in expenses:
#         if min_amount <= expense["amount"] <= max_amount:
#             print(
#                 "Amount:",expense["amount"],
#                 "Category:",expense["category"],
#                 "Date:",expense["date"],
#             )
#             found = True

#     if not found:
#         print("No expense found in this range.")
 
#  ###### 8.MONTHLY SUMMARY: #########
 
# def monthly_summary(expenses):
#     if len(expenses) == 0:
#         print("No expense recorded yet.")
#         return
    
#     monthly_totals={}
    
#     for expense in expenses:
#         month = expense["date"][:7]
        
#         if month not in monthly_totals:
#             monthly_totals[month]=0
            
#         monthly_totals[month] += expense["amount"]

#     print("\nMonthly Expense Summary: ")
#     for month in sorted(monthly_totals):
#         print(month,"→",f"{monthly_totals[month]:,.2f}")
        
# ###### 9.Export Monthly Summary to CSV: #########

# def export_monthly_summary(expenses):
#     if len(expenses) == 0:
#         print("No expenses recorded yet.")
#         return
    
#     monthly_totals = {}
    
#     for expense in expenses:
#         month = expense["date"][:7]
        
#         if month not in monthly_totals:
#             monthly_totals[month] = 0
        
#         monthly_totals[month] += expense["amount"]
    
#     with open ("monthly_summary.csv", mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["month","total"])
        
#         for month in sorted(monthly_totals):
#             writer.writerow([month, f"{monthly_totals[month]:.2f}"])    
            
#     print("Monthly summary exported successfully!")
    
# ###### 10.EXPENSE STATISTICS (ANALYSIS): #########

# def expense_statistics(expenses):
#     if len(expenses) == 0:
#         print("No expenses recorded yet.")
#         return
    
#     amounts =[]
    
#     for expense in expenses:
#         amounts.append(expense["amount"])

#     highest_expense = max(amounts)
#     lowest_expense = min(amounts)
#     average_expense = sum(amounts) / len(amounts)
    
#     print("\nExpense Statistics:")
#     print("Highest Expense:",f"{highest_expense:,.2f}")
#     print("Lowest Expense:",f"{lowest_expense:,.2f}")
#     print("Average Expense:",f"{average_expense:,.2f}")
    
# ###### 11.Category-wise Expense Analysis #########

# def category_wise_analysis(expenses):
#     if len(expenses) == 0:
#         print("No expenses recorded yet.")
#         return
    
#     category_totals = {}
#     for expense in expenses:
#         category = expense["category"].lower()
        
#         if category not in category_totals:
#             category_totals[category] = 0
#         category_totals[category] += expense["amount"]
    
#     print("\nCategory-wise Expense Analysis: ")
    
#     for category in sorted(category_totals):
#         print(category,"→",f"{category_totals[category]:,.2f}")  
        
#  ###### 12.Budget Limit Warning: #########
 
#  #1: load budget :
 
# def load_budgets():
#     monthly_budget = {}
    
#     if not os.path.exists("budgets.csv"):
#         return monthly_budget
#     with open("budgets.csv", mode="r", newline="") as file:
#         reader = csv.DictReader(file)
        
#         for row in reader:
#             monthly_budget[row["month"]] = float(row["budget"])
            
#         return monthly_budget
    
#  #2: save budget :
 
# def save_budgets(monthly_budget):
#      with open("budgets.csv", mode="w", newline="") as file:
#         fieldnames = ["month","budget"]
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         for month, budget in monthly_budget.items():
#             writer.writerow({"month": month, "budget": f"{budget:.2f}"})
            

# ###### 13.Set Monthly Budget: #########
           
# def set_monthly_budget(budgets):
#     month = input("Enter month to set budget (YYYY-MM): ").strip()

#     try:
#         budget = float(input("Enter budget amount: ").strip())
#     except ValueError:
#         print("Invalid budget! Please enter a valid number.")
#         return

#     if budget <= 0:
#         print("Budget must be greater than zero.")
#         return

#     if month in budgets:
#         print(f"Budget for {month} already exists. Do you want to update it? (yes/no)")
#         choice = input().strip().lower()

#         if choice != "yes":
#             print("Budget not updated.")
#             return

#     budgets[month] = budget
#     save_budgets(budgets)

#     print(f"Budget for {month} set to {budget:.2f}")
            
# ###### 14.Budget Limit Warning: #########
# def check_budget_status(expenses, budgets):
#     if len(budgets) == 0:
#         print("No budgets set yet.")
#         return
    
#     month = input("Enter month to check budget status (YYYY-MM): ").strip()
    
#     if month not in budgets:
#         print(f"No budget set for {month}.")
#         return
    
#     budget = budgets[month]
#     total = 0
    
#     expenses = load_expenses()
    
#     for expense in expenses:
#         if expense["date"][:7] == month:
#             total += expense["amount"]
    
#     print(f"Budget for {month}: {budget:.2f}")
#     print(f"Total Expenses for {month}: {total:.2f}")
    
#     if total > budget:
#         over = total - budget
#         percent = (over / budget) * 100
#         print(f"⚠ Budget exceeded by {over:.2f} ({percent:.2f}%)")
#     elif total == budget:
#         print("You have exactly used your budget.")
#     else:
#         remaining = budget - total
#         percent = (remaining / budget) * 100
#         print(f"Budget remaining: {remaining:.2f} ({percent:.2f}%)")
   
# ##### 15.Top Spending Category: #########     
# def top_spending_category(expenses):
#     if len(expenses) == 0:
#         print("No expenses recorded.")
#         return

#     category_totals = {}

#     for expense in expenses:
#         category = expense["category"]

#         if category not in category_totals:
#             category_totals[category] = 0

#         category_totals[category] += expense["amount"]

#     top_category = max(category_totals, key=category_totals.get)

#     print("Top spending category:", top_category)
#     print("Amount spent:", f"{category_totals[top_category]:.2f}")
    
         
    
      
# ##################### Step 2: Menu #############################
# expenses = load_expenses()
# budgets = load_budgets()

# while True:
#     print("\n Expense Tracker")
#     print(" 1.Add Expense")
#     print(" 2.View Expense")
#     print(" 3.Show Total")
#     print(" 4.Delete Expense")
#     print(" 5.Filter by Category")
#     print(" 6.Filter by Date")
#     print(" 7.Filter by Amount")
#     print(" 8.Monthly Summary")
#     print(" 9.Export Monthly Summary to CSV")
#     print(" 10.Expense Statistics")
#     print(" 11.Category-wise Expense Analysis")
#     print(" 12.Set / Update Monthly Budget")
#     print(" 13.Check Monthly Budget Status")
#     print(" 14.Top Spending Category")      
#     print(" 15.Exit")
#     choice = input("Enter Your Choice: ")
    
# # ADD EXPESENSE: 
#     if choice == "1":
#         add_expense(expenses, budgets)   
           
# # VIEW ALL EXPENSES: 
#     elif choice == "2":
#         view_expenses(expenses)

# # CALCULATE TOTAL EXPENSES:
#     elif choice == "3":
#         total_expense(expenses)  

# # DELETE EXPENSES :
#     elif choice =="4":
#         delete_expenses(expenses) 

# # FILTER EXPNESES :
#     elif choice =="5":
#         filter_by_category(expenses)    
        
# # FILTER EXPNESES BY CATEGORY:
#     elif choice =="6":
#         filter_by_date(expenses)  
          
# # FILTER EXPNESES BY CATEGORY:
#     elif choice =="7":
#         filter_by_amount_range(expenses) 
           
# # MONTHLY EXXPENSES SUMMARY :
#     elif choice =="8":
#         monthly_summary(expenses)   
         
# # Export MONTHLY EXXPENSES SUMMARY :
#     elif choice =="9":
#         export_monthly_summary(expenses) 
        
# # EXPENSE STATISTICS :
#     elif choice =="10":
#         expense_statistics(expenses)    

# # CATEGORY-WISE EXPENSE ANALYSIS :
#     elif choice =="11":
#         category_wise_analysis(expenses)   
        
# # SET / UPDATE MONTHLY BUDGET :
#     elif choice =="12":
#         set_monthly_budget(budgets) 

# # CHECK MONTHLY BUDGET STATUS :
#     elif choice == "13":
#         check_budget_status(expenses, budgets)

# # TOP SPENDING CATEGORY :
#     elif choice == "14":
#         top_spending_category(expenses)
    
# # EXIT: 
#     elif choice == "15":
#         print("Goodbye!")
#         break
   
#     else:
#         print("Invalid Choice")

