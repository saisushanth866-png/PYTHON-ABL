print("RETAIL BILLING SYSTEM")

products = []

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")

    category = input(
        "Enter category (Grocery/Electronics/Clothing): "
    ).lower()

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    subtotal = quantity * price

    products.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "subtotal": subtotal
    })

# Calculate total subtotal
total_subtotal = sum(item["subtotal"] for item in products)

# Discount calculation
if total_subtotal > 5000:
    discount = total_subtotal * 0.10

elif total_subtotal >= 2500:
    discount = total_subtotal * 0.05

else:
    discount = 0

# Maximum concession limit
if discount > 1000:
    discount = 1000

discounted_total = total_subtotal - discount

# Tax calculation
total_tax = 0

for item in products:

    if item["category"] == "grocery":
        tax_rate = 0.05

    elif item["category"] == "electronics":
        tax_rate = 0.18

    elif item["category"] == "clothing":
        tax_rate = 0.12

    else:
        tax_rate = 0

    item["tax"] = item["subtotal"] * tax_rate
    total_tax += item["tax"]

final_amount = discounted_total + total_tax

# Display invoice
print("\n========== ITEMIZED INVOICE ==========")

for item in products:
    print(
        item["name"],
        "| Qty:", item["quantity"],
        "| Price:", round(item["price"], 2),
        "| Subtotal:", round(item["subtotal"], 2),
        "| Tax:", round(item["tax"], 2)
    )

print("--------------------------------------")
print("Total Subtotal: Rs.", round(total_subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Final Amount: Rs.", round(final_amount, 2))

print("======================================")