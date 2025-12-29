def tax(income):
    if income < 250000:
        return 0
    elif income < 500000:
        return income * 0.05
    elif income < 1000000:
        return income * 0.2
    return income * 0.3

while True:
    inc = int(input("Income (0 to exit): "))
    if inc == 0:
        break
    print("Tax:", tax(inc))
    print()
# This program calculates the tax based on income brackets. It continues to prompt the user for income until 0 is entered.
    # End of file Chapter_12/tax.py
    
