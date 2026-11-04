print("EMPLOYEE PAYROLL SYSTEM")

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount: "))

# Calculate allowances
hra = basic * 0.20
da = basic * 0.10

# Calculate overtime pay
overtime_pay = 200 * overtime_hours

# Calculate gross salary
gross_salary = basic + hra + da + overtime_pay + incentive

# Calculate deduction rate
if gross_salary < 20000:
    deduction_rate = 0.05

elif gross_salary < 40000:
    deduction_rate = 0.10

else:
    deduction_rate = 0.15

deduction = gross_salary * deduction_rate

# Calculate net salary
net_salary = gross_salary - deduction

# Display payroll statement
print("\n========== EMPLOYEE PAYROLL ==========")
print("Employee Name:", name)
print("Basic Salary: Rs.", basic)
print("HRA: Rs.", hra)
print("DA: Rs.", da)
print("Overtime Pay: Rs.", overtime_pay)
print("Incentive: Rs.", incentive)
print("Gross Salary: Rs.", gross_salary)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net_salary)

print("======================================")
