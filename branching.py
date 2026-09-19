kw_hours = int(input("Enter the KW hours used: "))

if kw_hours <= 1000:
    amount_owed = kw_hours * 0.07633
else:
    amount_owed = 1000 * 0.07633 + (kw_hours - 1000) * 0.09259

print(f"Amount owed is ${amount_owed:.5f}")