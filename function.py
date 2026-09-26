def circle_area(radius):
    pi = 3.14159
    return pi * radius ** 2


def total_with_tax(money, tax_rate):
    return money + (money * tax_rate)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


radius = float(input("Enter radius: "))
money = float(input("Enter the amount of money: "))
tax_percent = float(input("Enter the tax rate as a percent (for example, 6): "))
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

print(f"Circle area: {circle_area(radius):.2f}")
print(f"Total with tax: {total_with_tax(money, tax_percent / 100):.2f}")
print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.4f}")
