print("CAMPUS EVENT FINANCIAL MANAGEMENT")

venue = float(input("Enter venue cost: "))

equipment = float(input("Enter equipment cost: "))

catering = float(input("Enter catering cost: "))

transport = float(input("Enter transport cost: "))

certificates = float(input("Enter certificate cost: "))

participants = int(input("Enter number of participants: "))

fee = float(input("Enter registration fee per participant: "))

sponsorship = float(input("Enter sponsorship amount: "))

# Calculate total cost
total_cost = (
    venue + equipment + catering +
    transport + certificates
)

# Calculate participant contribution
contribution = participants * fee

# Calculate sponsorship shortfall
shortfall = total_cost - contribution - sponsorship

if shortfall < 0:
    shortfall = 0

# Calculate minimum registrations
remaining_cost = total_cost - sponsorship

if remaining_cost <= 0:
    break_even = 0

elif fee <= 0:
    break_even = -1

else:
    break_even = -(- (remaining_cost - participants * fee) // fee)
    break_even = max(0, int(break_even))

# Display financial report
print("\n========== CAMPUS EVENT FINANCIAL REPORT ==========")

print("Total Event Cost: Rs.", total_cost)
print("Participant Contribution: Rs.", contribution)
print("Sponsorship: Rs.", sponsorship)
print("Sponsorship Shortfall: Rs.", shortfall)

if break_even == -1:
    print("Break-even: Cannot be achieved through registration fees alone")

else:
    print("Minimum Registrations:", break_even)

if shortfall == 0:
    print("Status: Financial Target Achieved")
else:
    print("Status: Additional Funds Required")

print("===================================================")