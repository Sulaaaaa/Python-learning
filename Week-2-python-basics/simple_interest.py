principal = float(input("Enter principal amount: ₦"))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest



print(f"\n===== SIMPLE INTEREST CALCULATOR =====")
print(f"\nPrincipal Amount: ₦{principal:.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: ₦{simple_interest:.2f}")
print(f"Total Amount: ₦{total_amount:.2f}")
print(f"\n=======================================")