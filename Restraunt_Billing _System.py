import datetime

bill_number = 101

# Sample Menu
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Pasta": 180,
    "Fries": 100,
    "Coke": 50
}

# GST (Tax)
TAX_RATE = 0.18  # 18%

# Store selected items
order = {}

print("🍽️ Welcome to Cyber Cafe")
print("📋 Menu:")
for item, price in menu.items():
    print(f"  {item}: ₹{price}")

print("\n👉 Enter your order (type 'done' to finish):")

while True:
    item = input("Item name: ").title()
    if item == "Done":
        break
    if item not in menu:
        print("❌ Item not on the menu. Please try again.")
        continue
    try:
        quantity = int(input(f"Quantity of {item}: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    if item in order:
        order[item] += quantity
    else:
        order[item] = quantity

# Personal Details
Name=input('Enter Your Name:')
Phone=int(input('Enter The Phone Number:'))

# Calculate bill
print("\n🧾 Generating your bill...\n")
subtotal = sum(menu[item] * qty for item, qty in order.items())
tax = subtotal * TAX_RATE
total = subtotal + tax

# Print bill
print("=============== CYBER CAFE ==============")
print(f"🧾 Bill No: {bill_number}")
bill_number += 1
print(Name)
print(Phone)
print("Order Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("-------------------------------------")
for item, qty in order.items():
    print(f"{item:10} x {qty:<3} = ₹{menu[item]*qty}")
print("-------------------------------------")
print(f"Subtotal:      ₹{subtotal:.2f}")
print(f"GST (18%):      ₹{tax:.2f}")
print(f"Total Amount:  ₹{total:.2f}")
print("==========================================")
print("🙏 Thank you! Visit again!")








