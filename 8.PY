print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

quantity = int(input("Enter quantity produced: "))

material_per_unit = float(
    input("Enter material cost per unit: ")
)

labour_per_unit = float(
    input("Enter labour cost per unit: ")
)

machine_per_unit = float(
    input("Enter machine cost per unit: ")
)

wastage_percentage = float(
    input("Enter wastage percentage: ")
)

selling_price_per_unit = float(
    input("Enter selling price per unit: ")
)

target_profit_percentage = float(
    input("Enter target profit percentage: ")
)

# Cost calculations
material_cost = quantity * material_per_unit

wastage_cost = material_cost * wastage_percentage / 100

labour_cost = quantity * labour_per_unit

machine_cost = quantity * machine_per_unit

total_production_cost = (
    material_cost + wastage_cost +
    labour_cost + machine_cost
)

# Sales calculation
total_sales_value = quantity * selling_price_per_unit

# Profit or loss
profit = total_sales_value - total_production_cost

profit_percentage = (
    profit / total_production_cost
) * 100 if total_production_cost > 0 else 0

# Target checking
print("\n========== PRODUCTION REPORT ==========")

print("Quantity Produced:", quantity)
print("Material Cost: Rs.", round(material_cost, 2))
print("Wastage Cost: Rs.", round(wastage_cost, 2))
print("Labour Cost: Rs.", round(labour_cost, 2))
print("Machine Cost: Rs.", round(machine_cost, 2))

print("Total Production Cost: Rs.", round(total_production_cost, 2))
print("Total Sales Value: Rs.", round(total_sales_value, 2))
print("Profit/Loss: Rs.", round(profit, 2))
print("Profit Percentage:", round(profit_percentage, 2), "%")

if profit_percentage >= target_profit_percentage:
    print("Status: PROFIT TARGET ACHIEVED")
else:
    print("Status: PROFIT TARGET NOT ACHIEVED")

print("========================================")