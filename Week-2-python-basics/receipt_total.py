item1 = float(input("Enter price of item 1: ₦"))
item2 = float(input("Enter price of item 2: ₦"))
item3 = float(input("Enter price of item 3: ₦"))

total = item1 + item2 + item3

print(f" ===== RECEIPT =====")
print(f"Item 1: ₦{item1:.2f}")
print(f"Item 2: ₦{item2:.2f}")
print(f"Item 3: ₦{item3:.2f}")
print(f"Total: ₦{total:.2f}")
print(f"===================")