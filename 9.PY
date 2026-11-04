print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter travel budget in INR: "))

conversion_fee_percentage = float(
    input("Enter conversion fee percentage: ")
)

n = int(input("Enter number of expenses: "))

expenses = []

for i in range(n):
    print(f"\nExpense {i + 1}")

    category = input("Enter expense category: ")
    currency = input("Enter currency: ")
    amount = float(input("Enter amount: "))

    exchange_rate = float(
        input(f"Enter exchange rate of 1 {currency} in INR: ")
    )

    # Currency conversion
    converted_amount = amount * exchange_rate

    # Conversion fee
    conversion_fee = (
        converted_amount * conversion_fee_percentage / 100
    )

    final_amount = converted_amount + conversion_fee

    expenses.append({
        "category": category,
        "currency": currency,
        "original": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "final": final_amount
    })

# Calculate total expense
total_expense = sum(
    expense["final"] for expense in expenses
)

# Find largest expense category
largest_expense = max(
    expenses,
    key=lambda x: x["final"]
) if expenses else None

# Display travel report
print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:
    print(
        f"\nCategory: {expense['category']}"
    )
    print(
        f"Original: {expense['original']:.2f} "
        f"{expense['currency']}"
    )
    print("Converted: Rs.", round(expense["converted"], 2))
    print("Conversion Fee: Rs.", round(expense["fee"], 2))
    print("Final Amount: Rs.", round(expense["final"], 2))

print("\nTotal Expense: Rs.", round(total_expense, 2))

if largest_expense:
    print("Largest Expense Category:",
          largest_expense["category"])

print("Planned Budget: Rs.", budget)

if total_expense <= budget:
    print("Status: Within Budget")
else:
    print("Status: Over Budget")

print("===========================================")